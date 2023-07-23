import xlsxwriter

my_workbook = xlsxwriter.Workbook('Beyonnex_Weather_shopper.xlsx')
my_worksheet = my_workbook.add_worksheet('Weather Shopper Results')

# Formats
passed_format = my_workbook.add_format({'border': 1, 'valign': 'vcenter', 'text_wrap': True, 'fg_color': 'green'})
failed_format = my_workbook.add_format({'border': 1, 'valign': 'vcenter', 'text_wrap': True, 'fg_color': 'red'})
na_format = my_workbook.add_format({'border': 1, 'valign': 'vcenter', 'text_wrap': True, 'fg_color': 'orange'})
merge_format = my_workbook.add_format({'bold': 1, 'border': 1, 'align': 'center', 'valign': 'vcenter', 'fg_color': 'yellow'})
merge_format_test_scenario = my_workbook.add_format({'bold': 1, 'border': 1, 'align': 'center', 'valign': 'vcenter'})
bold = my_workbook.add_format({'bold': True, 'border': 1})

# Column sizes
my_worksheet.set_column('A:A', 35)
my_worksheet.set_column('B:B', 35)

# Heading names
my_worksheet.merge_range('A1:B1', 'Weather Shopper Results', merge_format)
my_worksheet.write('A2', 'Test Scenario', bold)
my_worksheet.write('B2', 'Result', bold)
my_worksheet.write('A2', 'Test Scenario', bold)

# Test scenarios
test_scenarios = ['Page Load', 'Get Temperature', 'Click to buy Moisturizers', 'Add first Moisturizer', 'Add second Moisturizer', 'Click to buy Sunscreens', 'Add first Sunscreen', 'Add second Sunscreen', 'Click Cart']

for counter, value in enumerate(test_scenarios):
    my_worksheet.write('A' + str(counter + 3), value)

