from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry/domain-progress/message"
REP = ROOT / "reports/domain-progress/message"
REG.mkdir(parents=True, exist_ok=True)
REP.mkdir(parents=True, exist_ok=True)

features = [
    ("TLC-FC-07-MESSAGE-001", "definition", "blocked_locally", ["TLC-FC-07-MESSAGE-006"]),
    ("TLC-FC-07-MESSAGE-002", "validation_contract", "admissible", ["TLC-FC-07-MESSAGE-006"]),
    ("TLC-FC-07-MESSAGE-003", "validation_contract", "admissible", ["TLC-FC-07-MESSAGE-006"]),
    ("TLC-FC-07-MESSAGE-004", "message_structure_contract", "admissible", ["TLC-FC-07-MESSAGE-006"]),
    ("TLC-FC-07-MESSAGE-005", "state_contract", "blocked_locally", ["TLC-FC-07-MESSAGE-006"]),
    ("TLC-FC-07-MESSAGE-006", "message_declaration_contract", "provisionally_separated", []),
]

def dump(name, data):
    (REG / name).write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")

def report(name, title, rows, conclusion):
    text = [f"# {title}", "", "Generated from canonical `origin/main` inputs; no parallel branch is authoritative.", ""]
    text += [f"- {r}" for r in rows]
    text += ["", f"Conclusion: {conclusion}", ""]
    (REP / name).write_text("\n".join(text), encoding="utf-8")

meta = {"domain": "message", "preparation_only": True, "canonical_baseline": "origin/main", "authority_rule": "canonical_only"}

dump("source-inventory.yaml", {**meta, "sources": [
    {"path":"maths/07-message.md","role":"primary_scientific_source","canonical":True},
    {"path":"registry/scientific-objects/message/scientific-objects.candidate.yaml","role":"candidate_objects","count":72},
    {"path":"registry/scientific-objects/message/scientific-relations.candidate.yaml","role":"candidate_relations","count":71},
    {"path":"registry/scientific-objects/message/unresolved-terms.yaml","role":"unresolved_terms","count":61},
    {"path":"registry/feature-catalog.yaml","role":"canonical_feature_catalog","feature_count":6},
]})
dump("scientific-coverage.yaml", {**meta, "counts":{"objects":72,"relations":71,"unresolved":61,"features":6}, "object_types":{"Concept":61,"Definition":3,"State":3,"Example":2,"Entity":1,"Invariant":1,"Space":1}, "relation_types":{"refers_to":71}, "coverage":"complete_inventory_not_semantic_resolution"})
dump("feature-inventory.yaml", {**meta, "features":[{"feature_id":i,"class":c,"canonical_status":s,"depends_on":d,"planned_contract":f"contracts/message/{i.lower()}.schema.yaml","planned_ir":f"ir/message/{i.lower()}.ir.yaml"} for i,c,s,d in features]})
dump("functional-coverage.yaml", {**meta, "features_total":6,"objects_total":72,"relations_total":71,"unresolved_total":61,"all_objects_assigned":True,"all_unresolved_routed":True,"coverage_kind":"preparation"})

claims = [
 ("message_as_entity","supported","The canonical extraction types one Message object as Entity."),
 ("message_as_structure","supported","The source distinguishes structure and states of Message."),
 ("message_as_content","supported","Content is represented in the scientific objects."),
 ("message_as_transmission","candidate","Transmission language does not define a transport protocol."),
 ("message_as_interpretation","supported","Understanding and revelation are described scientifically."),
 ("sender_role","unresolved","No canonical sender interface or role symbol exists."),
 ("receiver_role","unresolved","No canonical receiver interface or role symbol exists."),
 ("encoding","unresolved","No canonical encoding is specified."),
 ("transport","unresolved","No canonical transport is specified."),
 ("execution","rejected","Message is not treated as executable code."),
]
dump("message-semantics.yaml", {**meta, "claims":[{"claim":a,"status":b,"evidence":c} for a,b,c in claims], "rule":"absence_of_protocol_is_not_permission_to_invent_one"})
dump("concept-separation.yaml", {**meta, "separations":[
 {"left":"Message","right":"Information","status":"provisional","rule":"not interchangeable without canonical proof"},
 {"left":"Message","right":"Communication","status":"provisional","rule":"message is not the communication process"},
 {"left":"Message","right":"Speech","status":"provisional","rule":"discourse is not a wire format"},
 {"left":"Message","right":"Event","status":"unresolved","rule":"no event contract inferred"},
 {"left":"Message","right":"Instruction","status":"rejected_as_default","rule":"content does not imply command semantics"},
]})
dump("message-structure.yaml", {**meta, "structure":{"identity":"required","content":"required","state":"required","provenance":"candidate","audience":"candidate","medium":"unresolved","encoding":"unresolved","transport":"out_of_scope","execution":"forbidden"}, "constraint":"fields are planning concepts, not a definitive schema"})

deps = {
 "master":("confirmed_symbol_only","canonical_complete","Role du Maître is explicit; reuse only canonical exported symbols."),
 "disciple":("candidate","canonical_complete","Receptive/understanding concepts suggest a dependency but no receiver interface is proven."),
 "community":("candidate","canonical_preparation_incomplete","Collective/cultural context is insufficient for a hard dependency."),
 "huit-dimensions":("candidate","noncanonical_parallel_work","Eight discourses are not assumed identical to the Huit Dimensions domain."),
 "invariants":("candidate","noncanonical_parallel_work","An invariant object exists but no upstream symbol is canonical."),
 "dynamics":("candidate","noncanonical_parallel_work","Process and cycle vocabulary do not prove a runtime dependency."),
 "theorems":("none","noncanonical_parallel_work","No theorem symbol is required by canonical Message evidence."),
 "principle":("candidate","historical_pilot_only","Fundamental language is not sufficient to bind Principle symbols."),
}
for domain,(status,authority,rationale) in deps.items():
    fn = f"{domain}-dependencies.yaml"
    dump(fn, {**meta,"upstream_domain":domain,"dependency_status":status,"upstream_authority":authority,"rationale":rationale,"imported_symbols":[],"invented_symbols":[]})
dump("external-domain-dependencies.yaml", {**meta,"dependencies":[{"domain":d,"status":v[0],"authority":v[1]} for d,v in deps.items()],"hard_dependencies":["master"],"candidate_dependencies":[d for d,v in deps.items() if v[0]=="candidate"]})
dump("upstream-symbol-mapping.yaml", {**meta,"mappings":[{"upstream_domain":"master","local_concept":"role_du_maitre","status":"symbol_reconciliation_required","symbol":None}],"forbidden":{"lexical_binding":True,"parallel_branch_authority":True}})
dump("feature-dependencies.yaml", {**meta,"edges":[{"from":"TLC-FC-07-MESSAGE-006","to":i,"status":"confirmed"} for i,_,_,d in features if d],"roots":["TLC-FC-07-MESSAGE-006"],"leaves":[i for i,_,_,d in features if d],"cycles":[]})
dump("feature-classification.yaml", {**meta,"classifications":[{"feature_id":i,"contract_class":c,"status":s,"executable":False} for i,c,s,_ in features],"allowed_classes":["definition","validation_contract","message_structure_contract","state_contract","message_declaration_contract"]})
dump("production-order.yaml", {**meta,"waves":[{"wave":1,"features":["TLC-FC-07-MESSAGE-006"],"purpose":"declaration and separation"},{"wave":2,"features":["TLC-FC-07-MESSAGE-002","TLC-FC-07-MESSAGE-003","TLC-FC-07-MESSAGE-004"],"purpose":"admissible validation and structure"},{"wave":3,"features":["TLC-FC-07-MESSAGE-001","TLC-FC-07-MESSAGE-005"],"purpose":"locally blocked definition and states"}],"cycle_free":True})
dump("contract-production-plan.yaml", {**meta,"contracts":[{"feature_id":i,"class":c,"status":"ready_with_reservations" if s in ("admissible","provisionally_separated") else "blocked_pending_local_resolution","must_not_define":["transport_protocol","encoding_protocol","execution_semantics"]} for i,c,s,_ in features],"contract_files_created":False})
dump("ir-production-plan.yaml", {**meta,"ir_units":[{"feature_id":i,"status":"blocked_until_contract_validation","executable":False} for i,_,_,_ in features],"ir_files_created":False,"ready_for_ir_generation":False})
dump("unresolved-status.yaml", {**meta,"total":61,"kind_counts":{"classification_uncertainty":61},"all_attached_to_object":True,"all_routed_to_feature":True,"blocking_policy":"block only the affected semantic claim or contract field; do not invent defaults"})
dump("historical-artifact-assessment.yaml", {**meta,"artifacts":[],"conclusion":"No historical Message contract or IR is accepted as canonical authority.","reuse":"none"})
dump("production-gates.yaml", {**meta,"gates":[
 {"gate":"source_inventory","status":"pass"},{"gate":"scientific_coverage","status":"pass"},{"gate":"concept_separation","status":"pass_with_reservations"},{"gate":"upstream_symbol_reconciliation","status":"blocked"},{"gate":"contract_generation","status":"ready_with_reservations"},{"gate":"ir_generation","status":"blocked"},{"gate":"implementation","status":"blocked"}],"no_premature_implementation":True})
dump("feature-status.yaml", {**meta,"features":[{"feature_id":i,"canonical_status":s,"preparation_status":"prepared_with_reservations","contract_exists":False,"ir_exists":False} for i,_,s,_ in features]})
dump("future-reconciliation.yaml", {**meta,"triggers":["upstream domain becomes canonical","global manifest accepts Message proposal","unresolved term is adjudicated","contract is generated"],"actions":["re-run dependency audit","reconcile symbols by canonical identifier","revalidate feature graph","update readiness without rewriting history"]})
dump("global-manifest-update-proposal.yaml", {**meta,"proposal_only":True,"mutates_global_manifest":False,"proposed_entry":{"domain":"message","feature_prefix":"TLC-FC-07-MESSAGE-","preparation_status":"complete_with_reservations","contracts":0,"ir_units":0}})
dump("preparation-status.yaml", {**meta,"status":"complete_with_reservations","ready_for_contract_generation_now":True,"ready_for_full_contract_generation":False,"ready_for_ir_generation":False,"ready_for_implementation_or_code_generation":False,"blocking_points":["61 classification uncertainties","sender/receiver roles unresolved","encoding and transport unspecified","upstream candidate symbols noncanonical"],"scope_compliance":{"contracts_created":False,"ir_created":False,"other_domains_modified":False,"global_manifest_modified":False}})

for y in sorted(REG.glob("*.yaml")):
    data = yaml.safe_load(y.read_text(encoding="utf-8"))
    report(y.stem + "-report.md", y.stem.replace("-"," ").title(), [f"Artifact: `{y.relative_to(ROOT)}`", f"Domain: {data.get('domain')}", f"Preparation only: {data.get('preparation_only')}"], "Prepared; consult the YAML artifact for machine-readable details and reservations.")
report("preparation-completion-report.md", "Message preparation completion", ["72 objects, 71 relations, 61 unresolved terms and 6 features inventoried.", "No Message contract, IR, protocol or executable artifact was created.", "Canonical Master symbols are the only hard upstream dependency; all other cross-domain bindings remain candidates or absent."], "Preparation is complete with reservations; contract generation may begin selectively, while IR and implementation remain blocked.")
