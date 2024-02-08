def get_context(prompt_id):
    if prompt_id == 1:
        return [{"role": "system", "content": PROMPT_1}]
    else:
        Exception("Prompt unknown")


PROMPT_1 = """\
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
