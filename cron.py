from jinja2 import Environment, PackageLoader

from models import return_families, return_emails_to_send, dept_id_to_name
from helpers import BatchMail, strip_tags

env = Environment(loader=PackageLoader('cron', 'templates'), autoescape = True,
                               extensions = ['jinja2.ext.autoescape'])

MERGE_MAPPINGS = {
    "!PARENTFIRSTNAMES!": "ParentFirstNames",
    "!PARENTSFULLNAMES!": "ParentFullNames",
    "!CHILDFIRSTNAMES!": "ChildFirstNames",
    "!CHILDFULLNAMES!": "ChildFullNames",
    "!PARENTEMAILS!": "ParentEmails",
    "!CHILDEMAILS!": "ChildEmails",
}


emails_to_send = return_emails_to_send()

for email in emails_to_send:

    # TODO - save the email as set right now in case of issues/slow sending

    dept_name = dept_id_to_name(email.DepartmentId)
    family_list, family_names, family_emails = return_families(dept_name)

    mail = BatchMail()

    for parents, children in family_list.iteritems():

        merged_content = email.Content

        for tag, data in MERGE_MAPPINGS.iteritems():
            merged_content = merged_content.replace(tag, family_names[parents][data])

        send_to = []
        if email.email_parents:
            send_to = family_emails[parents]['Parents']
        if email.email_parents:
            send_to = family_emails[parents]['Children']

        # Uncomment when deployed hashtag safetyfirst hashtag alwaysuseprotection
        send_to = ['txl11@ic.ac.uk']

        # Time for templating
        template = env.get_template('email.html')
        output = template.render(content=merged_content)
        text_output = strip_tags(merged_content)

        msg = mail.queue_mail(email.Subject, ("Mums and Dads", "mumsanddads@imperial.ac.uk"),
                              send_to, html_body=output, text_body=text_output)
    mail.send_queue()


"""
The following tags will work:
!PARENTFIRSTNAMES!
!PARENTSFULLNAMES!
!CHILDFIRSTNAMES!
!CHILDFULLNAMES!
!PARENTEMAILS!
!CHILDEMAILS!
"""

