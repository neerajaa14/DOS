from level_db import Session, LevelPageContent

def add_level_content_to_database():
    session = Session()
    session.query(LevelPageContent).delete()

    # Add content to the database
    content_entries = [
         
        LevelPageContent(
            question='What is Full form of DoS',
            option1='Disk Operating System',
            option2='Denial of Service',
            option3='Distributed System',
            option4='Data Overload System',
            answer='Denial of Service',
            requires_input=0
        ),
        LevelPageContent(
            question='What is the primary goal of a DoS attack?',
            option1='To steal sensitive information',
            option2='To disrupt or deny access to a service',
            option3='To gain unauthorized access to a system',
            option4='To install malware on a target system',
            answer='To disrupt or deny access to a service',
            requires_input=0
        ),
         LevelPageContent(
            question='Which of the following is a type of DoS attack that floods a network with ICMP echo request (ping) packets?',
            option1='SYN Flood',
            option2='UDP Flood',
            option3='Ping Flood',
            option4='Sumrf attack',
            answer='Ping Flood',
            requires_input=0
        ),
        
        LevelPageContent(
            question='What is a common method to mitigate DoS attacks on a network?',
            option1='Implementing strong passwords',
            option2=' Installing antivirus software',
            option3='Using firewalls and intrusion detection systems (IDS)',
            option4='Encrypting sensitive data',
            answer='Using firewalls and intrusion detection systems (IDS)',
            requires_input=0
        ),
      
]

    for entry in content_entries:
        session.add(entry)

    session.commit()

    session.close()