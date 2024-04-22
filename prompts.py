def get_context(prompt_id):
    if prompt_id == 1:
        return [{"role": "system", "content": PROMPT_1}]
    elif prompt_id == "I":
        return [{"role": "system", "content": PROMPT_I}]
    elif prompt_id == "II":
        return [{"role": "system", "content": PROMPT_II}]
    elif prompt_id == "III":
        return [{"role": "system", "content": PROMPT_III}]
    elif prompt_id == "Ia":
        return [{"role": "system", "content": PROMPT_Ia}]
    elif prompt_id == "IIa":
        return [{"role": "system", "content": PROMPT_IIa}]
    elif prompt_id == "IIIa":
        return [{"role": "system", "content": PROMPT_IIIa}]
    elif prompt_id == "IV":
        return [{"role": "system", "content": PROMPT_IV}]
    elif prompt_id == "IVa":
        return [{"role": "system", "content": PROMPT_IVa}]
    elif prompt_id == "Va":
        return [{"role": "system", "content": PROMPT_Va}]
    else:
        Exception("Prompt unknown")


PROMPT_1 = """
Hi, can we do an exercise related to data privacy? Many websites have the "privacy policy", and a paper proposed that there are 10 categories of data practice in such privacy contents:

1. First Party Collection/Use: how and why a
service provider collects user information.
2. Third Party Sharing/Collection: how user information may be shared with or collected by
third parties.
3. User Choice/Control: choices and control
options available to users.
4. User Access, Edit, & Deletion: if and how
users may access, edit, or delete their information.
5. Data Retention: how long user information is
stored.
6. Data Security: how user information is protected.
7. Policy Change: if and how users will be informed about changes to the privacy policy.
8. Do Not Track: if and how Do Not Track signals3
for online tracking and advertising are
honored.
9. International & Specific Audiences: practices
that pertain only to a specific group of users
(e.g., children, Europeans, or California residents).
10. Other: additional sub-labels for introductory or general text, contact information, and
practices not covered by the other categories.

I have a specific task for you: The user will give you a sentence from some privacy contents, and you tell them which category of practices this sentence may contain. Pleasy only respond with the category.
"""

# Prompt I: Data category title
PROMPT_I = """
Websites and digital products have privacy policies. Each sentence in these privacy policies can be annotated with one or more data practice.  A data practice means how the data is used and processed by an organization. In current context, a data practice belongs to one of the following data practice categories. 
 
1. First Party Collection/Use.
2. Third Party Sharing/Collection.
3. User Choice/Control.
4. User Access, Edit, and Deletion.
5. Data Retention.
6. Data Security. 
7. Policy Change.
8. Do Not Track.
9. International and Specific Audiences.
10. Other.
 
I have a specific task for you: The user will give you a sentence from some privacy contents, and you tell them which category of practices this sentence may contain. Please only respond with the category.
"""

# Data category title with OPP-115 description
PROMPT_II = """
Websites and digital products have privacy policies. Each sentence in these privacy policies can be annotated with one or more data practice.  A data practice means how the data is used and processed by an organization. In current context, a data practice belongs to one of the following data practice categories. 
 
1. First Party Collection/Use: how and why a service provider collects user information.
2. Third Party Sharing/Collection: how user information may be shared with or collected by
third parties.
3. User Choice/Control: choices and control options available to users.
4. User Access, Edit, and Deletion: if and how users may access, edit, or delete their information.
5. Data Retention: how long user information is stored.
6. Data Security: how user information is protected.
7. Policy Change: if and how users will be informed about changes to the privacy policy.
8. Do Not Track: if and how Do Not Track signals for online tracking and advertising are
honored.
9. International and Specific Audiences: practices that pertain only to a specific group of users (e.g., children, Europeans, or California residents).
10. Other: additional sub-labels for introductory or general text, contact information, and
practices not covered by the other categories.
 
I have a specific task for you: The user will give you a sentence from some privacy contents, and you tell them which category of practices this sentence may contain. Please only respond with the category.
"""

# Data category title with extended description
PROMPT_III = """
Websites and digital products have privacy policies. Each sentence in these privacy policies can be annotated with one or more data practice. A data practice means how the data is used and processed by an organization. In current context, a data practice belongs to one of the following data practice categories. 
 
1. First Party Collection/Use: how and why a service provider collects user information. In first party collection the service provider that owns or operates the website/platform/service directly collect data from individuals. 
2. Third Party Sharing/Collection: how user information may be shared with or collected by
third parties. In third party sharing/collection an entity other than the service provider collects data from users through the service provider's platform. Third parties could include advertisers, analytic companies, or partner services that have their own data collection and privacy practices.
3. User Choice/Control: choices and control options available to users. Choice means giving individuals options as to how their personal information may be used. Specifically, choice relates to secondary uses of information—that is, uses beyond those necessary to complete the contemplated transaction. Control means privacy controls that allow individuals to manage use and sharing of their data. 
4. User Access, Edit, and Deletion: if and how users may access, edit, or delete their information.
5. Data Retention: how long user information is stored. All data should have retention period associated with it, retention period means maximum period the data will be stored. 
6. Data Security: how user information is protected. In particular, it means the security measures that ensures security of personal data, including encryption or storage of data on secure servers. 
7. Policy Change: if and how users will be informed about changes to the privacy policy.
8. Do Not Track: if and how Do Not Track signals for online tracking and advertising are
honored.
9. International and Specific Audiences: practices that pertain only to a specific group of users (e.g., children, Europeans, or California residents).
10. Other: additional sub-labels for introductory or general text, contact information, and
practices not covered by the other categories.
 
I have a specific task for you: The user will give you a sentence from some privacy contents, and you tell them which category of practices this sentence may contain. Please only respond with the category.
"""

# Prompt I: Data category title without Other category
PROMPT_Ia = """
Websites and digital products have privacy policies. Each sentence in these privacy policies can be annotated with one or more data practice.  A data practice means how the data is used and processed by an organization. In current context, a data practice belongs to one of the following data practice categories. 
 
1. First Party Collection/Use.
2. Third Party Sharing/Collection.
3. User Choice/Control.
4. User Access, Edit, and Deletion.
5. Data Retention.
6. Data Security. 
7. Policy Change.
8. Do Not Track.
9. International and Specific Audiences.

I have a specific task for you: The user will give you a sentence from some privacy contents, and you tell them which category of practices this sentence may contain. Please only respond with the category.
"""

# Data category title with OPP-115 description without Other category
PROMPT_IIa = """
Websites and digital products have privacy policies. Each sentence in these privacy policies can be annotated with one or more data practice.  A data practice means how the data is used and processed by an organization. In current context, a data practice belongs to one of the following data practice categories. 
 
1. First Party Collection/Use: how and why a service provider collects user information.
2. Third Party Sharing/Collection: how user information may be shared with or collected by
third parties.
3. User Choice/Control: choices and control options available to users.
4. User Access, Edit, and Deletion: if and how users may access, edit, or delete their information.
5. Data Retention: how long user information is stored.
6. Data Security: how user information is protected.
7. Policy Change: if and how users will be informed about changes to the privacy policy.
8. Do Not Track: if and how Do Not Track signals for online tracking and advertising are
honored.
9. International and Specific Audiences: practices that pertain only to a specific group of users (e.g., children, Europeans, or California residents).

I have a specific task for you: The user will give you a sentence from some privacy contents, and you tell them which category of practices this sentence may contain. Please only respond with the category.
"""

# Data category title with extended description without Other category
PROMPT_IIIa = """
Websites and digital products have privacy policies. Each sentence in these privacy policies can be annotated with one or more data practice. A data practice means how the data is used and processed by an organization. In current context, a data practice belongs to one of the following data practice categories. 
 
1. First Party Collection/Use: how and why a service provider collects user information. In first party collection the service provider that owns or operates the website/platform/service directly collect data from individuals. 
2. Third Party Sharing/Collection: how user information may be shared with or collected by
third parties. In third party sharing/collection an entity other than the service provider collects data from users through the service provider's platform. Third parties could include advertisers, analytic companies, or partner services that have their own data collection and privacy practices.
3. User Choice/Control: choices and control options available to users. Choice means giving individuals options as to how their personal information may be used. Specifically, choice relates to secondary uses of information—that is, uses beyond those necessary to complete the contemplated transaction. Control means privacy controls that allow individuals to manage use and sharing of their data. 
4. User Access, Edit, and Deletion: if and how users may access, edit, or delete their information.
5. Data Retention: how long user information is stored. All data should have retention period associated with it, retention period means maximum period the data will be stored. 
6. Data Security: how user information is protected. In particular, it means the security measures that ensures security of personal data, including encryption or storage of data on secure servers. 
7. Policy Change: if and how users will be informed about changes to the privacy policy.
8. Do Not Track: if and how Do Not Track signals for online tracking and advertising are
honored.
9. International and Specific Audiences: practices that pertain only to a specific group of users (e.g., children, Europeans, or California residents).
 
I have a specific task for you: The user will give you a sentence from some privacy contents, and you tell them which category of practices this sentence may contain. Please only respond with the category.
"""
# Data category title with extended description and examples
PROMPT_IV = """
Websites and digital products have privacy policies. I will give you a dataset of privacy policies, where privacy policies are divided into paragraph length segments and each segment is annotated with one or more data practice. A data practice means how the data is used and processed by an organization. In current context, a data practice belongs to one of the following data practice categories.

1. First Party Collection/Use: how and why a service provider collects user information. In first party collection the service provider that owns or operates the website/platform/service directly collect data from individuals. For instance, when a customer engages with the services of Amazon.com, Amazon collects data such as the products they have browsed, their purchasing choices, or their behavior patterns. When Amazon makes a product recommendation to customer based on this data, it can be referred to as first-party advertising. In this case, collection and use of personal data is identified as first party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is first-party. For example: "We collect", "Data you provide", "Information we collect", "Our servers", "Our cookies", "We use your data" "Data collected from your interaction with our services", "Information you submit", “We restrict access to personal information to our employees, contractors, and agents”, etc.
2. Third Party Sharing/Collection: how user information may be shared with or collected by third parties. In third party sharing/collection an entity other than the service provider collects data from users through the service provider's platform. Third parties could include advertisers, ad network companies, analytic companies, or partner services that have their own data collection and privacy practices. Third-party entities often work with a variety of first-party websites, collecting information on user profiles from diverse sources, including news, weather, entertainment, and travel websites. For instance, if a customer uses Amazon.com's services and Amazon utilizes details about the user that have been collected by companies other than itself, this is known as third-party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is third-party. For example: "Third-party providers", "External partners", "Ad networks", "Data we share" "Cookies from third-party advertisers", "Third-party cookies", "Third-party analytics", "Our partners’ services", “data processors”, etc.
3. User Choice/Control: choices and control options available to users. Choice means giving individuals options as to how their personal information may be used. Specifically, choice relates to secondary uses of information—that is, uses beyond those necessary to complete the contemplated transaction. Control means privacy controls that allow individuals to manage use and sharing of their data. Example for choice/control can be following: “opt-in”, “opt-out”, “cookie preference” (functional/recommended/essential/performance/advertising), “location data controls”, “privacy control”, “communication preference”, “do-not-track”, “do-not-sell”, “withdraw consent”, etc.
4. User Access, Edit, and Deletion: if and how users may access, edit, or delete their information. These are privacy rights-based choices. In privacy policies such provision can be found in the following keywords and phrases: "right to access", “rights you have”, "request a copy", "view your information", "download your data", "personal data report", "obtain a copy", “how do I change my information”, “ how can I move my information”, "data subject access request", “delete information”, etc.
5. Data Retention: how long user information is stored. Retention period outlines the time period for which personal information is stored and when it will be deleted or anonymized. Here are examples of some keywords, terms, and phrases that commonly identify "data retention" in privacy policies: "retention period", "how long we keep your data", “retaining your information”, "storage duration", "duration", "keep your data", “hold your information”, “hold your information any longer than we have to”, etc.
6. Data Security: how user information is protected. In particular, it means the security measures that ensures security of personal data, including encryption or storage of data on secure servers. It also includes processing user data to improve safety and reliability of products, services, and users. Here are examples of some keywords, terms, and phrases that commonly identify "data security" in privacy policies: “security, fraud and abuse prevention”, “information security”, “security tips”, “security measures”, “security features”, “security partners”, “security controls”, “encryption”, “data breach procedure”, “secure server”, “firewalls and antivirus software”, “appropriate technical and organizational measures to safeguard personal information”, etc.
7. Policy Change: if and how users will be informed about changes to the privacy policy. Here are examples of some keywords, terms, and phrases that commonly identify "policy change" in privacy policies: “notify you about upcoming changes”, “we change this privacy policy from time to time”, “email notification of privacy policy changes”, “notification of changes”, “revisions to this policy”, “policy update alert”, “how we will inform you”, etc.
8. Do Not Track: if and how Do Not Track signals for online tracking and advertising are honored. Examples of keywords, terms, and phrases that commonly reflect "Do Not Track" in privacy policies include: “you can switch off some cookies and similar tracking technologies”, “online tracking preferences”, “do not track”, “behavioral tracking opt-out”, “opting-out of tracking”, etc.
9. International and Specific Audiences: practices that pertain only to a specific group of users (e.g., children, Europeans, or California residents). This category outlines specific provisions that apply exclusively to certain categories of users, such as children, or residents of Europe, or individuals living in California. The privacy policy includes clauses for these distinct user groups. Here are examples of some keywords, terms, and phrases that commonly identify international audiences or specific audiences in privacy policies: “child permissions”, “special protection of children's personal data”, “age-specific guidelines”, “kids profile”, “parental consent”, “children and teens”, “international users”, “regional laws”, “GDPR” (General Data Protection Regulation for European users), “CCPA” (California Consumer Privacy Act for California residents), “COPPA” (Children's Online Privacy Protection Act), “ CIPA” (Children’s Internet Protection Act in United States), “specific audience considerations”, “disclosure and international transfers”, “supplemental privacy disclosures for certain services and regions”, etc.
10. Other: additional sub-labels for introductory or general text, contact information, and practices not covered by the other categories.

I have a specific task for you: The user will give you a sentence from some privacy contents, and you tell them which category of practices this sentence may contain. Please only respond with the category.
"""

# Data category title with extended description and examples without Other category
PROMPT_IVa = """
Websites and digital products have privacy policies. I will give you a dataset of privacy policies, where privacy policies are divided into paragraph length segments and each segment is annotated with one or more data practice. A data practice means how the data is used and processed by an organization. In current context, a data practice belongs to one of the following data practice categories.

1. First Party Collection/Use: how and why a service provider collects user information. In first party collection the service provider that owns or operates the website/platform/service directly collect data from individuals. For instance, when a customer engages with the services of Amazon.com, Amazon collects data such as the products they have browsed, their purchasing choices, or their behavior patterns. When Amazon makes a product recommendation to customer based on this data, it can be referred to as first-party advertising. In this case, collection and use of personal data is identified as first party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is first-party. For example: "We collect", "Data you provide", "Information we collect", "Our servers", "Our cookies", "We use your data" "Data collected from your interaction with our services", "Information you submit", “We restrict access to personal information to our employees, contractors, and agents”, etc.
2. Third Party Sharing/Collection: how user information may be shared with or collected by third parties. In third party sharing/collection an entity other than the service provider collects data from users through the service provider's platform. Third parties could include advertisers, ad network companies, analytic companies, or partner services that have their own data collection and privacy practices. Third-party entities often work with a variety of first-party websites, collecting information on user profiles from diverse sources, including news, weather, entertainment, and travel websites. For instance, if a customer uses Amazon.com's services and Amazon utilizes details about the user that have been collected by companies other than itself, this is known as third-party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is third-party. For example: "Third-party providers", "External partners", "Ad networks", "Data we share" "Cookies from third-party advertisers", "Third-party cookies", "Third-party analytics", "Our partners’ services", “data processors”, etc.
3. User Choice/Control: choices and control options available to users. Choice means giving individuals options as to how their personal information may be used. Specifically, choice relates to secondary uses of information—that is, uses beyond those necessary to complete the contemplated transaction. Control means privacy controls that allow individuals to manage use and sharing of their data. Example for choice/control can be following: “opt-in”, “opt-out”, “cookie preference” (functional/recommended/essential/performance/advertising), “location data controls”, “privacy control”, “communication preference”, “do-not-track”, “do-not-sell”, “withdraw consent”, etc.
4. User Access, Edit, and Deletion: if and how users may access, edit, or delete their information. These are privacy rights-based choices. In privacy policies such provision can be found in the following keywords and phrases: "right to access", “rights you have”, "request a copy", "view your information", "download your data", "personal data report", "obtain a copy", “how do I change my information”, “ how can I move my information”, "data subject access request", “delete information”, etc.
5. Data Retention: how long user information is stored. Retention period outlines the time period for which personal information is stored and when it will be deleted or anonymized. Here are examples of some keywords, terms, and phrases that commonly identify "data retention" in privacy policies: "retention period", "how long we keep your data", “retaining your information”, "storage duration", "duration", "keep your data", “hold your information”, “hold your information any longer than we have to”, etc.
6. Data Security: how user information is protected. In particular, it means the security measures that ensures security of personal data, including encryption or storage of data on secure servers. It also includes processing user data to improve safety and reliability of products, services, and users. Here are examples of some keywords, terms, and phrases that commonly identify "data security" in privacy policies: “security, fraud and abuse prevention”, “information security”, “security tips”, “security measures”, “security features”, “security partners”, “security controls”, “encryption”, “data breach procedure”, “secure server”, “firewalls and antivirus software”, “appropriate technical and organizational measures to safeguard personal information”, etc.
7. Policy Change: if and how users will be informed about changes to the privacy policy. Here are examples of some keywords, terms, and phrases that commonly identify "policy change" in privacy policies: “notify you about upcoming changes”, “we change this privacy policy from time to time”, “email notification of privacy policy changes”, “notification of changes”, “revisions to this policy”, “policy update alert”, “how we will inform you”, etc.
8. Do Not Track: if and how Do Not Track signals for online tracking and advertising are honored. Examples of keywords, terms, and phrases that commonly reflect "Do Not Track" in privacy policies include: “you can switch off some cookies and similar tracking technologies”, “online tracking preferences”, “do not track”, “behavioral tracking opt-out”, “opting-out of tracking”, etc.
9. International and Specific Audiences: practices that pertain only to a specific group of users (e.g., children, Europeans, or California residents). This category outlines specific provisions that apply exclusively to certain categories of users, such as children, or residents of Europe, or individuals living in California. The privacy policy includes clauses for these distinct user groups. Here are examples of some keywords, terms, and phrases that commonly identify international audiences or specific audiences in privacy policies: “child permissions”, “special protection of children's personal data”, “age-specific guidelines”, “kids profile”, “parental consent”, “children and teens”, “international users”, “regional laws”, “GDPR” (General Data Protection Regulation for European users), “CCPA” (California Consumer Privacy Act for California residents), “COPPA” (Children's Online Privacy Protection Act), “ CIPA” (Children’s Internet Protection Act in United States), “specific audience considerations”, “disclosure and international transfers”, “supplemental privacy disclosures for certain services and regions”, etc.

I have a specific task for you: The user will give you a sentence from some privacy contents, and you tell them which category of practices this sentence may contain. Please only respond with the category.
"""

PROMPT_Va = """
Websites and digital products have privacy policies. I will give you a dataset of privacy policies, where privacy policies are divided into paragraph length segments and each segment is annotated with one or more data practice. A data practice means how the data is used and processed by an organization. In current context, a data practice belongs to one of the following data practice categories.

1. First Party Collection/Use: how and why a service provider collects user information. In first party collection the service provider that owns or operates the website/platform/service directly collect data from individuals. For instance, when a customer engages with the services of company A, company A collects data such as the products they have browsed, their purchasing choices, or their behavior patterns. When company A makes a product recommendation to customer based on this data, it can be referred to as first-party advertising. In this case, collection and use of personal data is identified as first party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is first-party. For example: "We collect", "Data you provide", "Information we collect", "Our servers", "Our cookies", "We use your data" "Data collected from your interaction with our services", "Information you submit", “We restrict access to personal information to our employees, contractors, and agents”, etc.
2. Third Party Sharing/Collection: how user information may be shared with or collected by third parties. In third party sharing/collection an entity other than the service provider collects data from users through the service provider's platform. Third parties could include advertisers, ad network companies, analytic companies, or partner services that have their own data collection and privacy practices. Third-party entities often work with a variety of first-party websites, collecting information on user profiles from diverse sources, including news, weather, entertainment, and travel websites. For instance, if a customer uses Amazon.com's services and Amazon utilizes details about the user that have been collected by companies other than itself, this is known as third-party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is third-party. For example: "Third-party providers", "External partners", "Ad networks", "Data we share" "Cookies from third-party advertisers", "Third-party cookies", "Third-party analytics", "Our partners’ services", “data processors”, etc.
3. User Choice/Control: choices and control options available to users. Choice means giving individuals options as to how their personal information may be used. Specifically, choice relates to secondary uses of information—that is, uses beyond those necessary to complete the contemplated transaction. Control means privacy controls that allow individuals to manage use and sharing of their data. Example for choice/control can be following: “opt-in”, “opt-out”, “cookie preference” (functional/recommended/essential/performance/advertising), “location data controls”, “privacy control”, “communication preference”, “do-not-track”, “do-not-sell”, “withdraw consent”, etc.
4. User Access, Edit, and Deletion: if and how users may access, edit, or delete their information. These are privacy rights-based choices. In privacy policies such provision can be found in the following keywords and phrases: "right to access", “rights you have”, "request a copy", "view your information", "download your data", "personal data report", "obtain a copy", “how do I change my information”, “ how can I move my information”, "data subject access request", “delete information”, etc.
5. Data Retention: how long user information is stored. Retention period outlines the time period for which personal information is stored and when it will be deleted or anonymized. Here are examples of some keywords, terms, and phrases that commonly identify "data retention" in privacy policies: "retention period", "how long we keep your data", “retaining your information”, "storage duration", "duration", "keep your data", “hold your information”, “hold your information any longer than we have to”, etc.
6. Data Security: how user information is protected. In particular, it means the security measures that ensures security of personal data, including encryption or storage of data on secure servers. It also includes processing user data to improve safety and reliability of products, services, and users. Here are examples of some keywords, terms, and phrases that commonly identify "data security" in privacy policies: “security, fraud and abuse prevention”, “information security”, “security tips”, “security measures”, “security features”, “security partners”, “security controls”, “encryption”, “data breach procedure”, “secure server”, “firewalls and antivirus software”, “appropriate technical and organizational measures to safeguard personal information”, etc.
7. Policy Change: if and how users will be informed about changes to the privacy policy. Here are examples of some keywords, terms, and phrases that commonly identify "policy change" in privacy policies: “notify you about upcoming changes”, “we change this privacy policy from time to time”, “email notification of privacy policy changes”, “notification of changes”, “revisions to this policy”, “policy update alert”, “how we will inform you”, etc.
8. Do Not Track: if and how Do Not Track signals for online tracking and advertising are honored. Examples of keywords, terms, and phrases that commonly reflect "Do Not Track" in privacy policies include: “you can switch off some cookies and similar tracking technologies”, “online tracking preferences”, “do not track”, “behavioral tracking opt-out”, “opting-out of tracking”, etc.
9. International and Specific Audiences: practices that pertain only to a specific group of users (e.g., children, Europeans, or California residents). This category outlines specific provisions that apply exclusively to certain categories of users, such as children, or residents of Europe, or individuals living in California. The privacy policy includes clauses for these distinct user groups. Here are examples of some keywords, terms, and phrases that commonly identify international audiences or specific audiences in privacy policies: “child permissions”, “special protection of children's personal data”, “age-specific guidelines”, “kids profile”, “parental consent”, “children and teens”, “international users”, “regional laws”, “GDPR” (General Data Protection Regulation for European users), “CCPA” (California Consumer Privacy Act for California residents), “COPPA” (Children's Online Privacy Protection Act), “ CIPA” (Children’s Internet Protection Act in United States), “specific audience considerations”, “disclosure and international transfers”, “supplemental privacy disclosures for certain services and regions”, etc.

I have a specific task for you: The user will give you a sentence from some privacy contents, and you tell them which category of practices this sentence may contain. Please only respond with the category.
"""