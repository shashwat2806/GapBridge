# Revised Policy Document

## Original Policy Text

RISK MANAGEMENT POLICY
1. PURPOSE
This policy establishes the framework by which the organization identifies, assesses, and responds to cybersecurity and operational risks.
2. SCOPE
This policy applies to all business units, systems, and third-party relationships that may introduce risk to the organization's operations, data, or reputation.
3. RISK MANAGEMENT OBJECTIVES
The organization's risk management objectives are to protect critical assets, maintain regulatory compliance, and ensure business continuity. These objectives are reviewed and approved annually by senior leadership.
4. RISK IDENTIFICATION
Risks shall be identified through regular risk assessments, vulnerability scans, audits, and incident reviews. Business unit leaders are responsible for reporting newly identified risks to the risk management team.
5. RISK ASSESSMENT
Identified risks shall be assessed based on likelihood and potential impact, using a standardized scoring methodology. Assessment results are recorded in the organization's risk register.
6. RISK RESPONSE
For each identified risk, the organization shall determine an appropriate response: accept, mitigate, transfer, or avoid. Risk owners are responsible for implementing approved mitigation actions within agreed timeframes.
7. THIRD-PARTY RISK
Risks introduced by suppliers and third-party vendors shall be assessed prior to engagement and monitored throughout the relationship. High-risk vendors are subject to additional due diligence and periodic reassessment.
8. RISK REPORTING
A summary of key organizational risks shall be presented to senior leadership on a quarterly basis, including the status of mitigation efforts for high-priority risks.
9. ROLES AND RESPONSIBILITIES
The risk management team is responsible for maintaining the risk register and coordinating assessments. Department heads are responsible for identifying and reporting risks within their area of operation.
10. POLICY REVIEW
This policy and the associated risk management methodology shall be reviewed annually and updated to reflect changes in the organization's risk landscape.


## Added Provisions (Gap Remediation)

_The following sections address gaps identified against the NIST Cybersecurity Framework, grounded in retrieved guidance from the CIS MS-ISAC NIST CSF 2024 Policy Template Guide._

### GOVERN

**Governance: Understanding and Communication of Dependent Outcomes, Cybersecurity in Human Resources Practices**

The organization shall establish and communicate outcomes, capabilities, and services that it depends on, ensuring all relevant stakeholders are informed (GV.OC-05). This includes understanding the interdependencies with other third parties, as well as internal systems and services.

Moreover, the organization shall incorporate cybersecurity principles into human resources practices (GV.RR-04). This encompasses integrating cybersecurity awareness in recruitment, onboarding, training, and performance evaluation processes to foster a culture of cybersecurity responsibility among employees.

### IDENTIFY

Asset Management (ID.AM) Policy:

The organization shall maintain inventories of hardware, software, services, systems, and data throughout their life cycles, ensuring their accurate and up-to-date representation. This includes authorized network communication and internal and external network data flows (ID.AM-1, ID.AM-2, ID.AM-3). The organization shall also maintain inventories of services provided by suppliers (ID.AM-4).

Assets within the organization shall be prioritized based on classification, criticality, resources, and impact on the mission (ID.AM-5). Inventories of data and corresponding metadata for designated data types shall be maintained (ID.AM-7). All systems, hardware, software, services, and data shall be managed throughout their life cycles, adhering to established policies such as Access Control Policy, Account Management/Access Control Standard, Configuration Management Policy, Identification and Authentication Policy, Sanitization Secure Disposal Standard, Secure Configuration Standard (ID.AM-8).

Vulnerabilities in assets shall be identified, validated, and recorded (ID.RA-01). Compliance with this policy shall be monitored throughout the technology product and service life cycle, as part of the organization's Cybersecurity supply chain risk management plans, which may include activities that occur after the conclusion of a partnership or service agreement.

### PROTECT

Identity Management and Access Control Policy

The organization shall implement measures to manage identities and credentials for authorized users, services, and hardware (PR.AA-01). These identities shall be proofed and bound to credentials based on the context of interactions (PR.AA-02). Authentication of users, services, and hardware shall be enforced (PR.AA-03). The organization shall protect identity assertions by ensuring their protection, conveyance, and verification (PR.AA-04). Access permissions, entitlements, and authorizations shall be defined in a policy, managed, enforced, reviewed, and incorporate the principles of least privilege and separation of duties (PR.AA-05).

Individuals in specialized roles shall receive awareness and training to possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind (PR.AT-02). Data at rest and data in transit shall be protected for confidentiality, integrity, and availability (PR.DS-01 and PR.DS-02). The organization shall establish, communicate, maintain, and improve plans and other cybersecurity policies that affect operations.

### DETECT

**DETECT Function Policy**

The organization shall implement measures for the detection of potentially adverse events within its systems, networks, physical environment, and personnel activities, as outlined by the following controls:

1. DE.AE-02: Potentially adverse events shall be analyzed to better understand associated activities.
2. DE.CM-01: Networks and network services shall be monitored to find potentially adverse events.
3. DE.CM-02: The physical environment shall be monitored to find potentially adverse events.
4. DE.CM-03: Personnel activity and technology usage shall be monitored to find potentially adverse events.
5. DE.AE-06: Information on adverse events shall be provided to authorized staff and tools.
6. DE.AE-07: Cyber threat intelligence and other contextual information shall be integrated into the analysis.
7. DE.AE-08: Incidents shall be declared when adverse events meet the defined incident criteria.

The detection of adverse events shall encompass vulnerability scanning, security logging, and the understanding of inherent risks to inform risk response prioritization. The organization shall establish processes for receiving, analyzing, and responding to vulnerability disclosures as per ID.RA-08.

### RESPOND

**Respond Function Policy**

The Organization shall implement a robust Incident Response Plan (IRP) that adheres to the NIST Cybersecurity Framework's RESPOND requirements. Upon incident declaration, the IRP shall be executed in collaboration with relevant third parties (RS.MA-01).

Incident reports, once triaged and validated (RS.MA-02), shall be categorized and prioritized based on their potential impact (RS.MA-03). Incidents requiring elevation or escalation shall be appropriately managed (RS.MA-04). The criteria for initiating incident recovery shall be applied in a timely manner (RS.MA-05).

Internal and external stakeholders shall be notified of incidents, with information shared consistently in accordance with response plans (RS.CO-02 and RS.CO-03). Additionally, the root cause analysis for each incident shall be performed to establish what transpired during the incident (RS.AN-03).

Communication methods and messaging in incident reporting and recovery shall utilize approved channels (as per the Computer Security Threat Response Policy, Contingency Planning Policy, Cyber Incident Response Standard, and Incident Response Policy).

### RECOVER

**Recovery Policy**

The organization shall execute the recovery portion of the incident response plan once initiated from the incident response process (RC.RP-01). Recovery actions shall be selected, scoped, prioritized, and performed (RC.RP-02), ensuring that the integrity of backups and other restoration assets is verified before their use for restoration (RC.RP-03).

The integrity of restored assets shall be verified, systems and services shall be restored, and normal operating status shall be confirmed (RC.RP-05). The end of incident recovery shall be declared based on predefined criteria, and all incident-related documentation shall be completed (RC.RP-06).

Recovery activities and progress in restoring operational capabilities shall be communicated to designated internal and external stakeholders (RC.CO-03), and public updates on incident recovery shall be shared using approved methods and messaging (RC.CO-04).
