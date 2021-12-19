import pandas as pd

organisation_to_search = "National Science Foundation"

agencies_list = [['Department of Agriculture', '$2.7B'], ['Department of Commerce', '$2.8B'], ['Department of Defense', '$36B'],
     ['Department of Health and Human Services', '$7.0B'], ['Department of the Interior', '$1.5B'],
     ['Department of Justice', '$3.1B'], ['Department of Labor', '$819M'], ['Department of State', '$2.6B'],
     ['Department of the Treasury', '$5.4B'], ['Social Security Administration', '$2.0B'],
     ['Department of Education', '$1.0B'], ['Department of Energy', '$3.1B'],
     ['Environmental Protection Agency', '$385M'], ['Department of Transportation', '$3.5B'],
     ['General Services Administration', '$765M'], ['Department of Homeland Security', '$7.4B'],
     ['Department of Housing and Urban Development', '$447M'],
     ['National Aeronautics and Space Administration', '$2.2B'], ['Small Business Administration', '$129M'],
     ['Department of Veterans Affairs', '$9.1B'], ['U.S. Agency for International Development', '$256M'],
     ['U.S. Army Corps of Engineers', '$275M'], ['National Archives and Records Administration', '$99.9M'],
     ['National Science Foundation', '$136M'], ['Nuclear Regulatory Commission', '$141M']]

for item in agencies_list:
     if organisation_to_search in item[0]:
          pass
