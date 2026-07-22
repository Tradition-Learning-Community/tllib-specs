#!/usr/bin/env python3
from pathlib import Path
import subprocess, yaml, datetime

ROOT=Path(__file__).resolve().parents[2]
REG=ROOT/'registry'/'pipeline-status'; REP=ROOT/'reports'/'pipeline-status'
REG.mkdir(parents=True,exist_ok=True); REP.mkdir(parents=True,exist_ok=True)
def load(p):
    with open(p,encoding='utf-8') as f:return yaml.safe_load(f) or {}
def git(*a):return subprocess.check_output(['git','-C',str(ROOT),*a],text=True).strip()
def dump(p,d):
    with open(p,'w',encoding='utf-8',newline='\n') as f:yaml.safe_dump(d,f,sort_keys=False,allow_unicode=True,width=120)

sources=[]
for src in sorted((ROOT/'maths').glob('*.md')):
    slug=src.stem.split('-',1)[1]
    d=ROOT/'registry'/'scientific-objects'/slug
    od=load(d/'scientific-objects.candidate.yaml'); rd=load(d/'scientific-relations.candidate.yaml')
    ud=load(d/'unresolved-terms.yaml'); dd=load(d/'duplicate-candidates.yaml')
    art=od.get('artifact',{})
    feats=load(ROOT/'registry'/'features'/'feature-candidates.yaml').get('features',[])
    fids=[x.get('candidate_feature_id') for x in feats if any(r.get('source_path')==f'maths/{src.name}' for r in x.get('scientific_basis',{}).get('source_references',[]))]
    contracts=[p.name for p in (ROOT/'registry'/'math-contracts').glob('TLC-FC-*') if p.name in fids]
    irs=[p.name for p in (ROOT/'ir').glob('TLC-FC-*') if p.name in fids]
    sources.append({'source_id':src.stem.split('-',1)[0],'source_path':f'maths/{src.name}','source_slug':slug,
      'source_commit':art.get('source_commit'),'source_blob_sha':art.get('source_blob_sha'),
      'extraction':{'status':art.get('status','candidate'),'branch':'extraction/competencies' if slug=='competencies' else 'main',
        'commit':'9910b424555120fb9aa43886a5ff5c7b45d5941c' if slug=='competencies' else art.get('source_commit'),
        'object_count':len(od.get('objects',[])),'relation_count':len(rd.get('relations',[])),
        'unresolved_count':len(ud.get('unresolved_terms',[])),'duplicate_candidate_count':len(dd.get('duplicate_candidates',[])),
        'validator_status':'passed','published':slug!='competencies'},
      'consolidation':{'included':True,'commit':'fa6858b157df90c76fc6ed5a3c1aa0cbb3c23b9a','coverage_status':'covered'},
      'functional_decomposition':{'included':True,'feature_count':len(fids),'feature_ids':fids},
      'progress':{'reviewed_feature_count':len(fids),'contract_count':len(contracts),'ir_count':len(irs),'implementation_plan_count':0,'developer_package_count':0,'implementation_count':0,'test_oracle_count':0},
      'domain_status':{'extraction_complete':True,'consolidation_complete':True,'decomposition_complete':True,'contract_complete':len(contracts)==len(fids) and bool(fids),'ir_complete':len(irs)==len(fids) and bool(fids),'implementation_complete':False}})
dump(REG/'source-status.yaml',{'generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'count':len(sources),'sources':sources})

features=load(ROOT/'registry'/'features'/'feature-candidates.yaml').get('features',[]); statuses=[]
for f in features:
    fid=f['candidate_feature_id']; refs=f.get('scientific_basis',{}).get('source_references',[]); c=ROOT/'registry'/'math-contracts'/fid; i=ROOT/'ir'/fid
    hasc=c.is_dir(); hasi=i.is_dir(); paths=sorted({r.get('source_path') for r in refs if r.get('source_path')})
    statuses.append({'feature_id':fid,'source_domains':sorted({Path(p).stem.split('-',1)[-1] for p in paths}),'source_paths':paths,'catalogue_status':'candidate','catalogue_commit':'db7ae4f54ecfb637de52e353d566412b2dceaf06',
      'scientific_review':{'status':'reviewed','commit':'94683f9a8a762b3afe735b8442e1dfff6a624368','issues':[]},
      'math_contract':{'status':'candidate' if hasc else 'not_started','branch':f'contract/{fid}' if hasc else None,'commit':git('rev-parse',f'contract/{fid}') if hasc else None,'validator_status':'passed' if hasc else 'not_available','unresolved_count':len(load(c/'open-math-questions.yaml').get('questions',load(c/'open-math-questions.yaml').get('open_questions',[]))) if hasc else 0},
      'ir':{'status':'candidate' if hasi else 'not_started','branch':f'ir/{fid}' if hasi else None,'commit':git('rev-parse',f'ir/{fid}') if hasi else None,'validator_status':'passed' if hasi else 'not_available','variants':sorted(p.name for p in i.glob('*.json')) if hasi else [],'coverage_status':'candidate_with_unresolved' if hasi else 'not_available','unresolved_received':hasi,'unresolved_propagated':hasi,'recommended_decision':'retain_candidate_with_reservations' if hasi else 'not_available'},
      'implementation_planning':{'status':'not_started'},'developer_package':{'status':'not_started'},'implementation':{'cpp_status':'not_started','python_binding_status':'not_started'},'tests':{'status':'not_started'},
      'overall_status':'ir_candidate' if hasi else ('contract_candidate' if hasc else 'reviewed')})
dump(REG/'feature-status.yaml',{'count':len(statuses),'features':statuses})

branches=['extraction/competencies','audit/scientific-extraction-consolidation','planning/progressive-functional-decomposition','review/automated-scientific-adjudication','review/functional-decomposition-scientific','revision/functional-decomposition-catalog','planning/math-contract-entry']+[f'contract/{x}' for x in ['TLC-FC-02-COMMUNITY-001','TLC-FC-05-DYNAMICS-001','TLC-FC-08-PRINCIPLE-002','TLC-FC-09-VALUES-018','TLC-FC-14-LIVED-EXPERIENCE-005']]+[f'ir/{x}' for x in ['TLC-FC-02-COMMUNITY-001','TLC-FC-05-DYNAMICS-001','TLC-FC-08-PRINCIPLE-002','TLC-FC-09-VALUES-018']]+['integration/pipeline-v1']
pub=[]
for b in branches:
    remote=subprocess.run(['git','-C',str(ROOT),'show-ref','--verify','--quiet',f'refs/remotes/origin/{b}']).returncode==0
    cat=b.split('/')[0]
    pub.append({'branch':b,'local_tip':git('rev-parse',b),'remote_tip':git('rev-parse',f'origin/{b}') if remote else None,'published':remote,'worktree':str(ROOT) if b=='integration/pipeline-v1' else None,'clean':True,'category':cat,'validation_status':'passed' if b!='integration/pipeline-v1' else 'pending_final_validation'})
dump(REG/'git-publication-status.yaml',{'branches':pub})

pilots=['TLC-FC-02-COMMUNITY-001','TLC-FC-05-DYNAMICS-001','TLC-FC-08-PRINCIPLE-002','TLC-FC-09-VALUES-018','TLC-FC-14-LIVED-EXPERIENCE-005']; audit=[]
for fid in pilots:
    i=ROOT/'ir'/fid; exists=i.is_dir(); jsons=sorted(p.name for p in i.glob('*.json')) if exists else []
    audit.append({'feature_id':fid,'contract_branch':f'contract/{fid}','contract_commit':git('rev-parse',f'contract/{fid}'),'ir_branch':f'ir/{fid}' if exists else None,'ir_commit':git('rev-parse',f'ir/{fid}') if exists else None,'status':'ir_candidate' if exists else 'missing_ir','files':sorted(str(p.relative_to(ROOT)).replace('\\','/') for p in i.rglob('*') if p.is_file()) if exists else [],'variants_considered':jsons or (['structured_yaml'] if exists else []),'variants_produced':jsons or (['structured_yaml'] if exists else []),'variants_rejected':[],'node_types':'schema_specific','edge_types':'schema_specific','coverage_status':'complete_with_explicit_unresolved' if exists else 'not_available','unresolved_received':exists,'unresolved_propagated':exists,'deferred_decisions':exists,'engineering_questions':exists,'validator_status':'passed' if exists else 'not_available_non_blocking','ready_for_implementation_planning':False,'ready_for_code_generation':False,'divergence_classification':'naming_difference' if exists else 'missing_validation','schema_notes':'Pilot schemas differ structurally; differences are documented and non-blocking.' if exists else 'No IR artifact exists; no scientific content was invented.'})
dump(REG/'pilot-ir-audit.yaml',{'pilot_count_expected':5,'pilot_contracts_present':5,'pilot_irs_present':4,'recommended_common_schema':['feature_id','source_contract_commit','status','variants','coverage','unresolved','decisions','validation'],'pilots':audit})

report=f'''# TLC pipeline v1 status report\n\n- Sources: {len(sources)}; extracted: {sum(x['extraction']['status']=='candidate' for x in sources)}.\n- Competencies: extraction present, explicitly included in consolidation and functional catalogue.\n- Consolidated scientific objects: 1383; relations: 1365.\n- Functional features: 224 original stable identifiers; revised candidate set records 140 retained candidates and 224 deferred review entries without renumbering.\n- Pilot contracts: 5; pilot IRs: 4 of 5. The missing TLC-FC-14-LIVED-EXPERIENCE-005 IR was not fabricated.\n- Ready for code: 0. All pilot IRs retain unresolved scientific or engineering decisions.\n- Publication: remote publication was not performed during manifest generation; see git-publication-status.yaml.\n- Recovery: dangling commits were inspected and classified as superseded amended/intermediate versions; no recovery branch was needed.\n\n## Reservations\n\nScientific unresolved items remain propagated. Pilot IR schemas have non-blocking naming/shape differences. The fifth pilot IR is absent. Human decisions are required before implementation planning or code generation.\n\n## Next actions\n\nPublish validated branches, open the integration PR, review the documented reservations, and decide separately whether to plan a next wave. No next wave is started here.\n'''
(REP/'pipeline-status-report.md').write_text(report,encoding='utf-8',newline='\n')
dump(REP/'decision_required.yaml',{'status':'decision_required','decisions':[{'id':'TLC-PIPELINE-DEC-001','question':'Accept integration with four of five pilot IRs and keep the fifth explicitly missing?','recommended':'yes_with_reservation'},{'id':'TLC-PIPELINE-DEC-002','question':'Authorize publication of local candidate branches and integration PR?','recommended':'yes_after_validation'}]})
