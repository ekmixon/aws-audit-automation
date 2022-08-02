import json
import pprint

data = json.loads(open('output/role-details.json').read())

for role in data:
	role_data = data[role]

	if 'AssumeRolePolicyDocument' not in role_data:
		continue

	statements = role_data['AssumeRolePolicyDocument']['Statement']

	if len(statements) > 1:
		print(role)
		pprint.pprint(statements)
		continue

	# "Action": "sts:AssumeRoleWithSAML",
	first_statement = statements[0]

	if first_statement['Action'] == 'sts:AssumeRoleWithSAML':
		continue

	principals = first_statement['Principal']
	if 'Service' not in principals:
		print(role)
		pprint.pprint(statements)
		continue

	services = first_statement['Principal']['Service']
	if isinstance(services, str):
		services = [services]

	should_continue = all(
		service.endswith('.amazonaws.com') for service in services
	)

	if should_continue:
		continue

	print(role)
	pprint.pprint(statements)
