# Revised Policy Document

## Original Policy Text

DATA PRIVACY AND SECURITY POLICY
1. PURPOSE
This policy establishes the organization's requirements for protecting personal and sensitive data collected, processed, and stored across all systems.
2. SCOPE
This policy applies to all employees, contractors, and third parties who handle organizational data, including customer information, employee records, and confidential business data.
3. DATA CLASSIFICATION
All data must be classified according to its sensitivity level: Public, Internal, Confidential, or Restricted. Data owners are responsible for assigning the appropriate classification at the time of creation.
4. DATA HANDLING
Employees must handle data in accordance with its classification level. Confidential and Restricted data must not be shared with unauthorized parties, whether internal or external to the organization.
5. THIRD-PARTY DATA SHARING
Before any personal or sensitive data is shared with external vendors or partners, a data protection agreement must be signed. The organization maintains a list of approved third-party data processors.
6. DATA RETENTION
Data shall be retained only as long as necessary to fulfill the purpose for which it was collected, subject to applicable legal and regulatory requirements. Retention schedules are reviewed annually by the compliance team.
7. INCIDENT NOTIFICATION
In the event of a suspected data breach, employees must notify the IT Security team within 24 hours of discovery. The organization will assess the scope of the breach and notify affected parties as required by applicable law.
8. EMPLOYEE RESPONSIBILITIES
All employees who handle personal data are required to complete data privacy training annually. Failure to comply with this policy may result in disciplinary action.
9. POLICY REVIEW
This policy will be reviewed annually by the Data Protection Officer and updated as necessary to reflect changes in applicable law and organizational practice.


## Added Provisions (Gap Remediation)

_The following sections address gaps identified against the NIST Cybersecurity Framework, grounded in retrieved guidance from the CIS MS-ISAC NIST CSF 2024 Policy Template Guide._

### GOVERN

Cybersecurity Risk Management Strategy

The organization shall establish and maintain a robust cybersecurity risk management strategy that aligns with its mission and objectives, as outlined in GV.OC-01 and GV.RM-01. This strategy shall consider the needs and expectations of both internal and external stakeholders, as defined in GV.OC-02, and clearly communicate critical capabilities and services that are relied upon or expected by these stakeholders (GV.OC-04).

The organization shall also identify and communicate outcomes, capabilities, and services it depends on for its operations (GV.OC-05), and establish risk appetite and tolerance statements that are communicated and consistently maintained (GV.RM-02). The strategy shall include cybersecurity risk management activities in the enterprise risk management processes (GV.RM-03) and provide a strategic direction that outlines appropriate response options to manage identified risks (GV.RM-04).

Lines of communication for cybersecurity risks, including those from suppliers and other third parties, shall be established and enforced within the organization (GV.RM-05). A standardized method for calculating, documenting, categorizing, and prioritizing cybersecurity risks shall be established and communicated to all relevant parties (GV.RM-06). Lastly, strategic opportunities or positive risks shall be characterized and incorporated in organizational cybersecurity risk discussions (GV.RM-07).

### IDENTIFY

Asset Management Policy (ID.AM)

All hardware, software, services, systems, data, and network communication within the organization shall be inventoried and maintained throughout their life cycles in accordance with ID.AM-1, ID.AM-2, ID.AM-3, and ID.AM-4 of the NIST Cybersecurity Framework.

The inventory shall include representations of authorized network communication and internal and external network data flows (ID.AM-3) and services provided by suppliers (ID.AM-4).

Assets shall be prioritized based on classification, criticality, resources, and impact on the mission (ID.AM-5), with data inventories maintained for designated data types (ID.AM-7).

The organization shall manage systems, hardware, software, services, and data throughout their life cycles, including configuration management, secure disposal, and sanitization (ID.AM-8).

Cybersecurity roles and responsibilities for suppliers, customers, and partners shall be established, communicated, and coordinated internally and externally (GV.SC-03). Suppliers shall be known and prioritized by criticality (GV.SC-04), with requirements to address cybersecurity risks in supply chains established, prioritized, and integrated into contracts and other types of agreements (GV.SC-05).

Planning and due diligence shall be conducted to identify, validate, and record vulnerabilities in assets (ID.RA-01) and receive cyber threat intelligence from information sharing forums and sources (ID.RA-02).

### PROTECT

Title: Identity Management and Access Control Policy (PR.AA)

In accordance with the NIST Cybersecurity Framework's Protect function, this organization shall establish and enforce policies for managing identities and access control (PR.AA). Specifically:

1. The organization shall manage identities and credentials for authorized users, services, and hardware (PR.AA-01).
2. Identities shall be proofed and bound to credentials based on the context of interactions (PR.AA-02).
3. Users, services, and hardware shall be authenticated (PR.AA-03).
4. Identity assertions shall be protected, conveyed, and verified (PR.AA-04).
5. Access permissions, entitlements, and authorizations shall be defined in a policy, managed, enforced, and reviewed, incorporating the principles of least privilege and separation of duties (PR.AA-05).
6. Physical access to assets shall be managed, monitored, and enforced commensurate with risk (PR.AA-06).
7. Individuals in specialized roles shall be provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind (PR.AT-02).
8. Configuration management practices shall be established and applied (PR.PS-01), and software shall be maintained, replaced, and removed commensurate with risk (PR.PS-02).

These policies shall be communicated, maintained, and improved as part of the organization's overall cybersecurity plans that affect operations.

### DETECT

Title: Detect Function Policy – NIST Cybersecurity Framework

The organization shall implement measures to detect potentially adverse cyber events in accordance with the NIST Cybersecurity Framework (CSF). The following requirements shall be met:

1. Potentially adverse events shall be analyzed to better understand associated activities (DE.AE-02).
2. Information shall be correlated from multiple sources (DE.AE-03).
3. The estimated impact and scope of adverse events shall be understood (DE.AE-04).
4. Cyber threat intelligence and other contextual information shall be integrated into the analysis (DE.AE-07).
5. Incidents shall be declared when adverse events meet the defined incident criteria (DE.AE-08).
6. Networks, network services, and the physical environment shall be monitored to find potentially adverse events (DE.CM-01, DE.CM-02, DE.CM-06).

These activities shall support the overall objectives of system and information integrity by providing necessary information for risk response prioritization (ID.RA-05) and incident management (RS.MA).

### RESPOND

Title: Respond Function - Incident Management

The Organization shall implement a robust incident response plan that is executed in coordination with relevant third parties (RS.MA-01) upon the declaration of a cybersecurity incident. The plan encompasses the triage and validation of incident reports (RS.MA-02), followed by the categorization and prioritization of incidents (RS.MA-03). As required, incidents shall be escalated or elevated to ensure effective management (RS.MA-04).

The criteria for initiating incident recovery shall be applied consistently with approved methods and messaging (RS.MA-05). Internal and external stakeholders shall be notified of incidents promptly in compliance with response plans, and information sharing shall occur only as designated (RS.CO-02 & RS.CO-03).

Upon the detection of a potential adverse event, analysis shall be conducted to establish what transpired during the incident and determine its root cause (RS.AN-03), utilizing established monitoring systems such as security logging standards and system and information integrity policy.

### RECOVER

Section: Incident Recovery and Communication (RC)

The organization shall execute the recovery portion of the incident response plan (RC.RP-01) upon initiation from the incident response process in accordance with the NIST Cybersecurity Framework. The recovery actions shall be selected, scoped, prioritized, and performed (RC.RP-02). The integrity of backups and other restoration assets shall be verified before utilizing them for restoration (RC.RP-03). Critical mission functions and cybersecurity risk management considerations shall guide the establishment of post-incident operational norms (RC.RP-04).

Upon restoring assets, their integrity shall be confirmed, systems and services shall be restored, and normal operating status shall be confirmed (RC.RP-05). The end of incident recovery shall be declared based on established criteria, and incident-related documentation shall be completed (RC.RP-06). Recovery activities and progress in restoring operational capabilities shall be communicated to designated internal and external stakeholders (RC.CO-03). Public updates on the incident recovery process shall be shared using approved methods and messaging (RC.CO-04).
