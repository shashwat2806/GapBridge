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

_The following sections address gaps identified against the NIST Cybersecurity Framework, grounded in retrieved guidance from the CIS MS-ISAC NIST CSF 2024 Policy Template Guide._

### GOVERN

**Governance: Understanding and Communicating Critical Cybersecurity Dependencies and Risks**

The Organization shall establish, communicate, and maintain a clear understanding of the critical objectives, capabilities, and services that stakeholders depend on or expect from the Organization (GV.OC-04, GV.OC-05). Additionally, the Organization shall identify and communicate outcomes, capabilities, and services it depends on (GV.OC-05).

The risk appetite and risk tolerance of the Organization shall be established, communicated, and maintained (GV.RM-02). Furthermore, a strategic direction that describes appropriate risk response options shall be established and communicated (GV.RM-04).

Cybersecurity considerations shall be integrated into human resources practices (GV.RR-04). The cybersecurity roles and responsibilities for suppliers, customers, and partners shall be established, communicated, and coordinated internally and externally (GV.SC-02). Suppliers shall be known and prioritized by criticality (GV.SC-04), and requirements to address cybersecurity risks in supply chains shall be established, prioritized, and integrated into contracts and other types of agreements with suppliers and relevant third parties (GV.SC-05).

Planning and due diligence shall be performed to reduce risks before entering into formal supplier or third-party relationships (GV.SC-06). The risks posed by a supplier, their products and services, and other third parties shall be understood, recorded, prioritized, assessed, responded to, and monitored over the course of the relationship (GV.SC-07). Relevant suppliers and other third parties shall be included in incident planning, response, and recovery activities (GV.SC-08), and supply chain security practices shall be integrated into cybersecurity and enterprise risk management programs (GV.SC-09).

The cybersecurity risk management strategy outcomes shall be reviewed to inform and adjust strategy and direction (GV.OV-01, GV.OV-02), and organizational cybersecurity risk management performance shall be evaluated and reviewed for necessary adjustments (GV.OV-03).

### IDENTIFY

Asset Management Policy (ID)

The organization shall maintain inventories of all hardware, software, services, systems, network communication, internal and external data flows, services provided by suppliers, data, and corresponding metadata for designated data types. This inventory shall be managed throughout the life cycle of each asset. The prioritization of assets shall be based on their classification, criticality, resources required, and impact on the organization's mission. Vulnerabilities in these assets shall be identified, validated, and recorded.

Compliance with this policy shall be monitored throughout the technology product and service life cycle. The organization shall implement appropriate policies, standards, and procedures for Acceptable Use of Information Technology Resources, Access Control, Account Management/Access Control, Identification and Authentication, Information Classification, System and Communications Protection, Configuration Management, Sanitization Secure Disposal, Secure Configuration, and Maintenance to ensure adherence. Additionally, the organization shall manage cybersecurity supply chain risk in accordance with established plans and procedures.

This policy is intended to promote a secure and organized approach to asset management within the organization, ensuring that all assets are properly identified, prioritized, and managed throughout their life cycles, while also identifying and addressing vulnerabilities in a timely manner.

### PROTECT

Identity Management and Access Control Policy

1. The organization shall manage identities and credentials for authorized users, services, and hardware (PR.AA-01).
2. Identities shall be proofed and bound to credentials based on the context of interactions (PR.AA-02).
3. Users, services, and hardware shall be authenticated (PR.AA-03).
4. Identity assertions shall be protected, conveyed, and verified (PR.AA-04).
5. Access permissions, entitlements, and authorizations shall be defined in a policy, managed, enforced, and reviewed, incorporating the principles of least privilege and separation of duties (PR.AA-05).
6. Individuals in specialized roles shall receive awareness and training to perform tasks with cybersecurity risks in mind (PR.AT-02).
7. The confidentiality, integrity, and availability of data-at-rest shall be protected (PR.DS-01), as well as the confidentiality, integrity, and availability of data-in-transit (PR.DS-02).

### DETECT

Section: Detention of Potentially Adverse Events (DE)

The Organization shall implement measures to effectively detect potentially adverse cybersecurity events, aligning with the NIST Cybersecurity Framework's Detect function.

1. DE.AE-02: The Organization shall analyze potential adverse events to better comprehend associated activities and improve incident response strategies.
2. DE.AE-03: Information from multiple sources shall be correlated for a comprehensive understanding of the security landscape.
3. DE.AE-04: The Organization shall understand the estimated impact and scope of adverse events, enabling informed decision-making and prioritization of responses.
4. DE.AE-06: Information on adverse events shall be provided to authorized staff and tools for efficient response and mitigation efforts.
5. DE.AE-07: Cyber threat intelligence and other contextual information shall be integrated into the analysis, providing a more robust and informed understanding of the security situation.
6. DE.AE-08: Incidents shall be declared when adverse events meet the defined incident criteria, triggering the execution of the incident response plan.
7. DE.CM-01: Networks and network services shall be monitored to find potentially adverse events, ensuring proactive detection and response.
8. DE.CM-02: The physical environment shall also be monitored for potentially adverse events, extending the Organization's security surveillance beyond digital assets.

### RESPOND

Title: Respond Function of the Organizational Cybersecurity Policy

The organization shall adopt a comprehensive incident response plan that is executed in coordination with relevant third parties upon declaring an incident (RS.MA-01). This plan shall include procedures for triaging and validating incident reports (RS.MA-02), categorizing and prioritizing incidents (RS.MA-03), and escalating or elevating incidents as needed (RS.MA-04).

Upon categorization, the criteria for initiating recovery shall be applied (RS.MA-05). Internal and external stakeholders shall be notified of incidents in accordance with established response plans (RS.CO-02 & RS.CO-03), with information shared consistently and appropriately.

The root cause of each incident shall be analyzed to establish what has taken place during the incident (RS.AN-03). This analysis shall be conducted using approved methods and messaging, and shall be monitored for potentially adverse events in accordance with relevant standards.

### RECOVER

**Recovery Policy**

The organization shall implement the Recovery portion of the incident response plan in accordance with the initiated incident response process (RC.RP-01). Upon initiation, recovery actions shall be selected, scoped, prioritized, and performed (RC.RP-02). The integrity of backups and other restoration assets must be verified before their utilization for restoration (RC.RP-03).

Upon the successful verification and restoration of assets, systems, and services, normal operating status shall be confirmed (RC.RP-05). The end of incident recovery shall be declared based on predefined criteria, and related documentation shall be completed (RC.RP-06).

Communication of recovery activities and progress in restoring operational capabilities shall be shared with designated internal and external stakeholders (RC.CO-03). Public updates on the incident recovery process shall be shared using approved methods and messaging (RC.CO-04).

In all cases, this policy shall adhere to the Computer Security Threat Response Policy, Cyber Incident Response Standard, Incident Response Policy, and Contingency Planning Policy as required by NIST.
