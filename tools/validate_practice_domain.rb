#!/usr/bin/env ruby
require 'yaml'
features = YAML.load_file('registry/domain-progress/practice/functional-coverage.yaml', aliases: true).fetch('features').map { |f| f.fetch('feature_id') }
abort("expected 10 features, found #{features.length}") unless features.length == 10
features.each do |fid|
  c="registry/math-contracts/#{fid}/contract.yaml"; i="registry/ir/#{fid}/ir.yaml"; t="registry/test-plans/#{fid}/test-plan.yaml"
  [c,i,t].each { |p| abort("missing #{p}") unless File.file?(p); YAML.load_file(p, aliases: true) }
  ir=YAML.load_file(i, aliases: true); tp=YAML.load_file(t, aliases: true)
  abort("IR feature mismatch #{fid}") unless ir['feature_id']==fid
  abort("IR contract mismatch #{fid}") unless ir['contract_ref']==c
  abort("test plan feature mismatch #{fid}") unless tp['feature_id']==fid
  abort("test plan contract mismatch #{fid}") unless tp['contract_ref']==c
  abort("test plan ir mismatch #{fid}") unless tp['ir_ref']==i
end
new_artifacts = Dir.glob('{registry/math-contracts,registry/ir,registry/test-plans}/**/artifact.yaml')
abort("artifact.yaml present: #{new_artifacts.join(', ')}") unless new_artifacts.empty?
maths_changes = `git diff --name-only -- maths/`.split("\n")
abort("maths modified: #{maths_changes.join(', ')}") unless maths_changes.empty?
puts "practice domain validation passed: #{features.length} features, #{features.length} contracts, #{features.length} IRs, #{features.length} test plans"
