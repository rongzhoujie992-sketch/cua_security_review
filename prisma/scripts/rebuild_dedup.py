#!/usr/bin/env python3
from pathlib import Path
import csv, re, unicodedata, urllib.parse, collections

def norm_text(s):
    s=unicodedata.normalize("NFKC",s or "").casefold()
    s=s.replace("–","-").replace("—","-").replace("−","-")
    s=re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?"," ",s)
    s=s.replace("{","").replace("}","").replace("$","").replace("\\"," ")
    s=re.sub(r"[^a-z0-9]+"," ",s)
    return " ".join(s.split())

def norm_title(s): return norm_text(s)

def norm_doi(s):
    s=(s or "").strip().casefold()
    s=re.sub(r"^https?://(?:dx\.)?doi\.org/","",s)
    s=re.sub(r"^doi:\s*","",s)
    return s.rstrip(" .,/")

def base_arxiv(s):
    s=(s or "").strip()
    s=re.sub(r"^https?://arxiv\.org/(?:abs|pdf)/","",s)
    s=s.removesuffix(".pdf")
    return re.sub(r"v\d+$","",s)

def canonical_url(s):
    s=(s or "").strip()
    if not s:return ""
    u=urllib.parse.urlsplit(s)
    host=u.netloc.casefold()
    if host.startswith("www."): host=host[4:]
    path=re.sub(r"/+$","",u.path)
    if host=="arxiv.org":
        m=re.search(r"/(?:abs|pdf)/([^/?#]+)",path)
        if m:return "https://arxiv.org/abs/"+base_arxiv(m.group(1))
    pairs=urllib.parse.parse_qsl(u.query,keep_blank_values=True)
    keep=[]
    for k,v in pairs:
        kl=k.casefold()
        if kl.startswith("utm_") or kl in {"hl","source","ved","sa","ei","oq"}: continue
        keep.append((k,v))
    keep.sort()
    q=urllib.parse.urlencode(keep,doseq=True)
    return urllib.parse.urlunsplit(("https",host,path,q,""))

VERSION_SEPARATE_TITLES={norm_title(x) for x in [
    "Riosworld: Benchmarking the risk of multimodal computer-use agents",
    "Mcp safety audit: Llms with the model context protocol allow major security exploits",
    "AgentLeak: A Benchmark for Internal-Channel Privacy Leakage in Multi-Agent LLM Systems",
    "Agents under siege: Breaking pragmatic multi-agent llm systems with optimized prompt attacks",
    "Explainable and fine-grained safeguarding of llm multi-agent systems via bi-level graph anomaly detection",
    "GUI-360: A Comprehensive Dataset and Benchmark for Computer-Using Agents",
    "Your agent can defend itself against backdoor attacks",
]}
MANUAL_SAME_REPORT_TITLES={norm_title(x) for x in [
    "A Survey on Challenges and Emerging Frontiers of Multi-Agent Systems",
    "Towards the versioning of LLM-agent-based software",
]}

def main():
    root=Path(__file__).resolve().parents[1]
    inp=root/"dedup"/"global_occurrence_ledger.csv"
    with open(inp,newline="",encoding="utf-8-sig") as f:
        rows=list(csv.DictReader(f))
    n=len(rows); assert n==18371,n
    parent=list(range(n));rank=[0]*n;edges=[]
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]];x=parent[x]
        return x
    def union(a,b,rule):
        ra,rb=find(a),find(b)
        if ra==rb:return False
        if rank[ra]<rank[rb]:ra,rb=rb,ra
        parent[rb]=ra
        if rank[ra]==rank[rb]:rank[ra]+=1
        edges.append((a,b,rule))
        return True
    def union_by(items,rule):
        seen={}
        for i,k in items:
            if not k:continue
            if k in seen:union(i,seen[k],rule)
            else:seen[k]=i
    union_by(((i,base_arxiv(r["arxiv_id"])) for i,r in enumerate(rows) if r["arxiv_id"]),"arxiv_id")
    union_by(((i,r["acl_id"].casefold()) for i,r in enumerate(rows) if r["acl_id"]),"acl_id")
    union_by(((i,norm_doi(r["doi"])) for i,r in enumerate(rows) if r["doi"] and r["source"]!="arXiv"),"doi_non_arxiv")
    union_by(((i,canonical_url(r["primary_url"])) for i,r in enumerate(rows) if r["primary_url"]),"canonical_report_url")
    union_by(((i,r["source"]+"|"+r["source_native_id"].casefold()) for i,r in enumerate(rows) if r["source_native_id"] and r["source"]!="Google Scholar"),"source_native")
    gs_by_title=collections.defaultdict(list)
    for i,r in enumerate(rows):
        if r["source"]=="Google Scholar" and r["title"]:
            gs_by_title[norm_title(r["title"])].append(i)
    for t,ids in sorted(gs_by_title.items()):
        comps=collections.defaultdict(list)
        for i in ids: comps[find(i)].append(i)
        if len(comps)<2 or t in VERSION_SEPARATE_TITLES: continue
        reps=[min(v) for _,v in sorted(comps.items())]
        anchor=reps[0]
        for j in reps[1:]:
            ya,yb=rows[anchor]["year"],rows[j]["year"]
            if ya and yb and ya.isdigit() and yb.isdigit() and abs(int(ya)-int(yb))>1: continue
            rule="manual_same_report_copy" if t in MANUAL_SAME_REPORT_TITLES else "exact_title_generic_report_copy"
            union(anchor,j,rule)
    comps=collections.defaultdict(list)
    for i in range(n): comps[find(i)].append(i)
    ordered=sorted(comps.values(),key=min)
    idx_to_rec={}
    for k,ids in enumerate(ordered,1):
        rec=f"REC-{k:05d}"
        for i in ids: idx_to_rec[i]=rec
    assert len(ordered)==10090,len(ordered)
    assert len(edges)==8281,len(edges)
    mapout=root/"dedup"/"occurrence_to_record_REBUILT.csv"
    with open(mapout,"w",newline="",encoding="utf-8-sig") as f:
        w=csv.DictWriter(f,fieldnames=["occurrence_id","record_id","source","query_id"])
        w.writeheader()
        for i,r in sorted(enumerate(rows),key=lambda item:(idx_to_rec[item[0]],item[0])):
            w.writerow({"occurrence_id":r["occurrence_id"],"record_id":idx_to_rec[i],"source":r["source"],"query_id":r["query_id"]})
    edgeout=root/"dedup"/"dedup_edges_REBUILT.csv"
    with open(edgeout,"w",newline="",encoding="utf-8-sig") as f:
        w=csv.DictWriter(f,fieldnames=["edge_id","left_occurrence_id","right_occurrence_id","dedup_rule","result_record_id"])
        w.writeheader()
        for k,(a,b,rule) in enumerate(edges,1):
            w.writerow({"edge_id":f"DE-{k:05d}","left_occurrence_id":rows[a]["occurrence_id"],"right_occurrence_id":rows[b]["occurrence_id"],"dedup_rule":rule,"result_record_id":idx_to_rec[a]})
    print("DEDUP REBUILD: PASS")
    print("records=10,090 duplicates_removed=8,281")

if __name__=="__main__": main()
