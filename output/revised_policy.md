# Revised Policy Document

## Original Policy Text

Information Security Management Policy
1. Purpose
This policy establishes the framework for managing information security risks across the organization.
2. Scope
This policy applies to all employees, contractors, and systems that access organizational data.
3. Access Control
Users must have unique login credentials. Multi factor authentication is required for all critical systems.
4. Risk Management
Risk assessments must be conducted annually to identify vulnerabilities and threats.


## Added Provisions (Gap Remediation)

_The following sections address gaps identified against the NIST Cybersecurity Framework._

### GOVERN

Section: Governance – GOVERN Function of the NIST Cybersecurity Framework

All critical objectives, capabilities, and services that stakeholders depend on or expect from the Organization shall be identified, understood, and clearly communicated (GV.OC-04). Similarly, outcomes, capabilities, and services that the Organization depends on shall also be recognized and disseminated (GV.OC-05).

Risk appetite and tolerance statements must be established, communicated, and consistently maintained throughout the organization (GV.RM-02). Furthermore, a strategic direction that outlines suitable risk response options shall be developed and broadcasted (GV.RM-04).

To ensure effective cybersecurity management, human resources practices must incorporate cybersecurity considerations (GV.RR-04). Additionally, roles and responsibilities for suppliers, customers, and partners regarding cybersecurity shall be defined, communicated, and coordinated internally and externally (GV.SC-02).

The Organization shall establish, prioritize, and integrate cybersecurity risk management requirements into contracts and other agreements with suppliers, customers, and relevant third parties (GV.SC-05). Furthermore, the Organization's supply chain shall include only known entities, prioritized by their criticality to the organization (GV.SC-04).

### IDENTIFY

**Section: Asset Management – Identification**

In alignment with the NIST Cybersecurity Framework, it is hereby mandated that the organization shall maintain accurate and current inventories of all hardware (ID.AM-1), software, services, and systems (ID.AM-2) under its management. The organization shall also create and maintain representations of authorized network communication and internal and external data flows (ID.AM-3).

The organization shall ensure that inventories of services provided by suppliers are kept up-to-date (ID.AM-4). Assets within the organization's domain shall be prioritized based on their classification, criticality, resources required, and potential impact on the organization's mission (ID.AM-5).

Inventories of designated data types and corresponding metadata shall be maintained (ID.AM-7), and the lifecycle management of all systems, hardware, software, services, and data shall be strictly adhered to (ID.AM-8). Furthermore, vulnerabilities in assets must be identified, validated, and duly recorded (ID.RA-01).

Compliance with these requirements is essential for the effective management of the organization's cybersecurity posture and will aid in the implementation of robust protective measures.

### PROTECT

Title: Identity Management and Access Control

The Organization shall establish and maintain a robust identity management system to ensure secure access control for authorized users, services, and hardware. This system shall comply with the following requirements:

1. PR.AA-01: All identities and credentials associated with the Organization's assets shall be managed in accordance with established policies and procedures.
2. PR.AA-02: The proofing and binding of identities to credentials shall be based on the context of user, service, or hardware interactions, ensuring secure authentication.
3. PR.AA-03: All users, services, and hardware shall undergo strict authentication processes to verify their identity before access is granted.
4. PR.AA-04: The Organization shall implement measures to protect identity assertions during transmission, conveyance, and verification to prevent unauthorized access or manipulation.
5. PR.AA-05: Access permissions, entitlements, and authorizations shall be defined in a policy, managed, enforced, and reviewed consistently. The principles of least privilege and separation of duties shall be incorporated into these access controls.
6. PR.AT-02: Individuals in specialized roles shall receive awareness training to ensure they possess the necessary knowledge and skills to perform their tasks while keeping cybersecurity risks in mind.
7. PR.DS-01: The confidentiality, integrity, and availability of data at rest within the Organization's systems shall be protected through appropriate measures.
8. PR.DS-02: Data in transit within the Organization's network shall also be protected to ensure its confidentiality, integrity, and availability.

### DETECT

Title: DETECT Function of the NIST Cybersecurity Framework

The Organization shall implement a robust DETECT function in accordance with the NIST Cybersecurity Framework, encompassing the following requirements:

1. Potentially adverse events shall be analyzed to enhance understanding of associated activities (DE.AE-02).
2. Information from multiple sources shall be correlated to identify potential threats and vulnerabilities (DE.AE-03).
3. The Organization shall understand the estimated impact and scope of adverse events to ensure effective response (DE.AE-04).
4. Authorized staff and tools shall be provided with information on adverse events for timely and informed action (DE.AE-06).
5. Cyber threat intelligence and contextual information shall be integrated into the analysis to strengthen risk assessment (DE.AE-07).
6. Incidents shall be declared when adverse events meet the defined incident criteria (DE.AE-08).
7. Networks and network services shall be continuously monitored to identify potentially adverse events (DE.CM-01).
8. The physical environment shall also be monitored to discover any potential threats or vulnerabilities (DE.CM-02).

The Organization's commitment to these measures ensures the continuous monitoring and analysis of potential cybersecurity threats, thereby enhancing overall security posture and response capabilities.

### RESPOND

Title: Incident Response - RESPOND Function Compliance with NIST Cybersecurity Framework

The organization shall establish and implement an incident response plan that is executed in coordination with relevant third parties upon the declaration of a cybersecurity incident (RS.MA-01). Upon receipt of incident reports, they must be triaged and validated (RS.MA-02). Incidents shall be categorized and prioritized based on their severity and potential impact (RS.MA-03). The incident response team shall escalate or elevate incidents as needed to ensure prompt action (RS.MA-04). The criteria for initiating incident recovery shall be strictly adhered to, following a thorough assessment of the incident's extent and potential damage (RS.MA-05).

In accordance with the NIST Cybersecurity Framework, internal and external stakeholders must be notified of incidents promptly (RS.CO-02), and communication channels shall be established for sharing pertinent information consistent with response plans (RS.CO-03). Root cause analysis shall be conducted to establish what transpired during an incident and the underlying factors contributing to its occurrence (RS.AN-03).

Upon completion of this analysis, corrective measures shall be implemented to mitigate future incidents and improve overall cybersecurity posture.

### RECOVER

Section: Recovery Function of Incident Response Plan

The organization shall execute the recovery portion of the incident response plan once initiated from the incident response process (RC.RP-01). In the event of an incident, recovery actions shall be selected, scoped, prioritized, and performed (RC.RP-02). The integrity of backups and other restoration assets must be verified before they are utilized for restoration (RC.RP-03). Upon completion of recovery activities, the integrity of restored assets shall be verified, systems and services shall be restored, and normal operating status shall be confirmed (RC.RP-05). The end of incident recovery shall be declared based on predetermined criteria, and all related documentation shall be completed (RC.RP-06).

Communication with designated internal and external stakeholders regarding recovery activities and progress in restoring operational capabilities is mandatory (RC.CO-03). Public updates on incident recovery shall be shared using approved methods and messaging (RC.CO-04).
