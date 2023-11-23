// You can reference the input variables using input.NAME
// Parsed JSON files could be referenced as fileInput
exports.step = function(input, fileInput) {
  input.Downloaded_contract_file.name = "ResponseFile"
	return input.Downloaded_contract_file;
};