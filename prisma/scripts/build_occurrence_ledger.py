#!/usr/bin/env python3
from pathlib import Path
import csv, re, xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
NS={"a":"http://www.w3.org/2005/Atom"}

def norm_doi(s):
    s=(s or "").strip().casefold()
    s=re.sub(r"^https?://(?:dx\.)?doi\.org/","",s)
    s=re.sub(r"^doi:\s*","",s)
    return s.rstrip(" .,/")

def base_arxiv(s):
    s=(s or "").strip()
    s=re.sub(r"^https?://arxiv\.org/(?:abs|pdf)/","",s).removesuffix(".pdf")
    return re.sub(r"v\d+$","",s)

pub={}; rawfile={}
for p in sorted((ROOT/"search/arxiv/raw").glob("*.xml")):
    rt=ET.fromstring(p.read_bytes())
    for e in rt.findall("a:entry",NS):
        aid=(e.findtext("a:id",default="",namespaces=NS) or "").strip().rsplit("/",1)[-1]
        pub[aid]=(e.findtext("a:published",default="",namespaces=NS) or "").strip()
        rawfile[aid]="arxiv/raw/"+p.name

rows=[]
with open(ROOT/"search/google_scholar/google_scholar_occurrence_ledger.csv",newline="",encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        rows.append({
            "occurrence_id":"GS:"+r["occurrence_id"],"source":"Google Scholar","query_id":r["run_id"],
            "source_native_id":r["occurrence_id"],"title":r["title"],"authors":r["authors_display"],
            "year":r["year"],"doi":norm_doi(r["doi"]),"arxiv_id":base_arxiv(r["arxiv_id"]),"acl_id":"",
            "primary_url":r["landing_page_url"],"source_url":r["scholar_result_url"],"published_date":"","raw_artifact":""
        })
with open(ROOT/"search/acl/acl_occurrences.csv",newline="",encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        rows.append({
            "occurrence_id":f'ACL:{r["run_id"]}:{r["source_native_id"]}',"source":"ACL Anthology","query_id":r["query_id"],
            "source_native_id":r["source_native_id"],"title":r["title"],"authors":r["authors"],"year":r["year"],
            "doi":norm_doi(r["doi"]),"arxiv_id":"","acl_id":r["source_native_id"],"primary_url":r["source_url"],
            "source_url":r["source_url"],"published_date":"","raw_artifact":"ACL official bulk snapshot"
        })
with open(ROOT/"search/arxiv/arxiv_occurrences.csv",newline="",encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        aid=r["arxiv_id"]
        rows.append({
            "occurrence_id":f'ARX:{r["run_id"]}:{aid}',"source":"arXiv","query_id":r["query_id"],
            "source_native_id":r["source_native_id"],"title":r["title"],"authors":r["authors"],"year":r["year"],
            "doi":norm_doi(r["doi"]),"arxiv_id":base_arxiv(aid),"acl_id":"","primary_url":r["source_url"],
            "source_url":r["source_url"],"published_date":pub.get(aid,""),"raw_artifact":rawfile.get(aid,"")
        })

with open(ROOT/"search/venue_checks/iclr_official_venue_check.csv",newline="",encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        rows.append({
            "occurrence_id":"ICLR:"+r["query_id"]+":"+r["source_native_id"],
            "source":r["source"],"query_id":r["query_id"],"source_native_id":r["source_native_id"],
            "title":r["title"],"authors":r["authors"],"year":r["year"],"doi":norm_doi(r["doi"]),
            "arxiv_id":base_arxiv(r["arxiv_id"]),"acl_id":r["acl_id"],"primary_url":r["primary_url"],
            "source_url":r["source_url"],"published_date":r["published_date"],
            "raw_artifact":"search/venue_checks/iclr_official_venue_check.csv"
        })
assert len(rows)==18371,len(rows)
out=ROOT/"dedup/global_occurrence_ledger_REBUILT.csv"
with open(out,"w",newline="",encoding="utf-8-sig") as f:
    fields=["occurrence_index"]+list(rows[0].keys())
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
    for i,r in enumerate(rows,1): w.writerow({"occurrence_index":i,**r})
print("OCCURRENCE LEDGER BUILD: PASS")
print("records=18,371")
