from config import newerpol, db

from schema import t_MumsandDadsAllocation

EMAIL_POSTFIX = "@imperial.ac.uk"

def return_email(username):
    return username + EMAIL_POSTFIX

def return_families(department):
    family_list = {}
    person_details = {}
    family_names = {}
    family_emails = {}

    all_results = newerpol.query(t_MumsandDadsAllocation).filter_by(OCNameTypeName=unicode(department), CurrentYear=1)

    for res in all_results:
        person_details[res.FirstParentLogin] = (res.FirstParentFName, res.FirstParent)
        person_details[res.SecondParentLogin] = (res.SecondParentFName, res.SecondParent)
        person_details[res.Login] = (res.ChildFname, res.ChildName)

        couple = (res.FirstParentLogin, res.SecondParentLogin)
        try:
            family_list[couple].append(res.Login)
        except KeyError:
            family_list[couple] = [res.Login]

    for parents, children in family_list.iteritems():

        family_names[parents] = {}
        family_names[parents]['ParentFirstNames'] = person_details[parents[0]][0] + " and " + person_details[parents[1]][0]
        family_names[parents]['ParentFullNames'] = person_details[parents[0]][1] + " and " + person_details[parents[1]][1]
        family_names[parents]['ParentEmails'] = parents[0] + EMAIL_POSTFIX + ", " + parents[1] + EMAIL_POSTFIX

        family_emails[parents] = {}
        family_emails[parents]['Parents'] = [return_email(parents[0]), return_email(parents[1])]

        num_children = len(children)

        child_names = ""
        for i in range(num_children - 2):
            child_names += person_details[children[i]][0] + ", "
        child_names += person_details[children[num_children - 2]][0] + " and " + person_details [children[num_children - 1]][0]
        family_names[parents]['ChildFirstNames'] = child_names

        child_names = ""
        for i in range(num_children - 2):
            child_names += person_details[children[i]][1] + ", "
        child_names += person_details[children[num_children - 2]][1] + " and " + person_details [children[num_children - 1]][1]
        family_names[parents]['ChildFullNames'] = child_names

        child_names = ""
        for i in range(num_children - 2):
            child_names += children[i] + EMAIL_POSTFIX + ", "
        child_names += children[num_children - 2] + EMAIL_POSTFIX + " and " + children[num_children - 1] + EMAIL_POSTFIX
        family_names[parents]['ChildEmails'] = child_names

        c_emails = []
        for i in children:
            c_emails.append(return_email(i))
        family_emails[parents]['Children'] = c_emails

    return family_list, family_names, family_emails


def return_emails_to_send():
    return db.MailMerges.filter(db.MailMerges.Sent==False)


def dept_id_to_name(dept_id):
    return db.Departments.filter(db.Departments.DepartmentId==dept_id)[0].DepartmentNameTypeName


if __name__ == "__main__":
    print return_families(u'Electrical & Electronic Engineering')