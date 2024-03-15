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

# Prompt I: Data category title
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

# Data category title with OPP-115 description
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

# Data category title with extended description
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
