# Revised Policy Document

## Original Policy Text

PATCH MANAGEMENT POLICY
1. PURPOSE
This policy defines the process for identifying, testing, and deploying software patches and security updates across the organization's systems and infrastructure.
2. SCOPE
This policy covers all servers, workstations, network devices, and applications owned or managed by the organization, including systems hosted on-premises and in the cloud.
3. PATCH IDENTIFICATION
The IT team is responsible for monitoring vendor security advisories and identifying applicable patches for all in-scope systems on a weekly basis.
4. PATCH PRIORITIZATION
Patches shall be prioritized based on the severity of the vulnerability they address. Critical security patches must be evaluated for deployment within 72 hours of release. Non-critical patches may follow the standard monthly maintenance cycle.
5. TESTING
Before deployment to production systems, patches must be tested in a non-production environment to confirm compatibility and stability. Testing results must be documented.
6. DEPLOYMENT
Approved patches shall be deployed according to the organization's change management process. Deployment windows are scheduled outside of business hours where possible to minimize disruption.
7. EXCEPTIONS
Systems that cannot be patched according to the standard schedule due to operational constraints must be documented as exceptions, along with compensating controls, and reviewed by IT leadership.
8. VERIFICATION
After deployment, the IT team shall verify that patches were applied successfully and that no unintended issues have occurred.
9. REPORTING
A monthly patch compliance report shall be generated, summarizing the patch status of all in-scope systems and any outstanding exceptions.
10. POLICY REVIEW
This policy shall be reviewed on an annual basis or following any significant change to the organization's IT infrastructure.


## Added Provisions (Gap Remediation)

_The following sections address gaps identified against the NIST Cybersecurity Framework, grounded in retrieved guidance from the CIS MS-ISAC NIST CSF 2024 Policy Template Guide._

### GOVERN

**Govern: Risk Management Strategy (GV.RM)**

The Organization shall establish and maintain risk management objectives that are aligned with the organizational mission and agreed upon by stakeholders (GV.RM-01). The Organization shall also define risk appetite and tolerance statements, communicating and updating them as necessary (GV.RM-02). Cybersecurity risk management activities and outcomes shall be incorporated into the enterprise risk management processes (GV.RM-03).

The Organization shall establish a strategic direction that describes appropriate risk response options, communicating this direction throughout the organization (GV.RM-04). Lines of communication for cybersecurity risks, including those from suppliers and other third parties, shall be established and maintained (GV.RM-05).

A standardized method for calculating, documenting, categorizing, and prioritizing cybersecurity risks shall be established and communicated within the Organization (GV.RM-06). The Organization shall also characterize strategic opportunities (positive risks) and include them in organizational cybersecurity risk discussions (GV.RM-07).

Organizational leadership is responsible and accountable for cybersecurity risk, fostering a culture that is risk-aware, ethical, and continually improving (GV.RR-01). Roles, responsibilities, and authorities related to cybersecurity risk management shall be established, communicated, understood, and enforced within the Organization (GV.RR-02).

### IDENTIFY

Section: Asset Management (ID.AM) - Identification and Inventory of Organizational Assets

The Organization shall maintain accurate inventories of all hardware, software, services, systems, data, and network communication flows managed by the Organization in accordance with ID.AM-1, ID.AM-2, ID.AM-3, ID.AM-4, ID.AM-7, and ID.AM-8 as specified by the NIST Cybersecurity Framework. These inventories shall be updated throughout the technology product and service life cycle.

The Organization's assets shall be prioritized based on classification, criticality, resources, and impact on the mission, in accordance with ID.AM-5.

The Organization shall identify, validate, and record vulnerabilities in its assets as outlined in ID.RA-01.

Throughout the life cycles of systems, hardware, software, services, and data, the Organization shall adhere to the relevant policies for Acceptable Use of Information Technology Resources, Access Control, Account Management/Access Control Standards, Identification and Authentication, Information Classification, Information Security, Security Assessment and Authorization, Configuration Management, Sanitization Secure Disposal Standard, Secure Configuration Standard, and Maintenance.

### PROTECT

**Protect: Identity Management and Access Control (PR)**

All authorized users, services, and hardware shall have their identities and credentials effectively managed by the organization according to the Access Control Policy, Account Management/Access Control Standard, Configuration Management Policy, Identification and Authentication Policy, Sanitization Secure Disposal Standard, and Secure Configuration Standard. These credentials must be proofed and bound to identities based on the context of interactions (PR.AA-02). The organization shall authenticate users, services, and hardware (PR.AA-03), and protect identity assertions during transmission and verification (PR.AA-04).

Access permissions, entitlements, and authorizations for all assets must be defined in a policy, managed, enforced, and reviewed consistently. The principles of least privilege and separation of duties shall be incorporated into the access management strategy (PR.AA-05). Physical access to organizational assets must be managed, monitored, and enforced commensurate with risk levels (PR.AA-06).

Personnel and individuals in specialized roles shall receive cybersecurity awareness and training to enable them to perform tasks with due consideration for potential risks (PR.AT-01 & PR.AT-02). Cybersecurity education and training shall be provided throughout the technology product and service life cycle, as outlined in the Security Awareness and Training Policy, Information Security Policy, Personnel Security Policy, Physical and Environmental Protection Policy, Access Control Policy, Account Management/Access Control Standard, Authentication Tokens Standard, Configuration Management Policy, Identification and Authentication Policy, and Acceptable Use of Information Technology Resource Policy.

### DETECT

**Detect Function Policy**

The organization shall implement measures that enable the timely identification of adverse cybersecurity events by monitoring both network and physical environments (DE.CM-01 & DE.CM-02). Potentially adverse events shall be analyzed to better understand associated activities (DE.AE-02), information correlated from multiple sources (DE.AE-03), and the estimated impact and scope of these events understood (DE.AE-04). The organization shall provide information on identified adverse events to authorized staff and tools (DE.AE-06) while integrating cyber threat intelligence and other contextual information into this analysis (DE.AE-07). Incidents shall be declared when adverse events meet the defined incident criteria (DE.AE-08). The organization shall ensure that all these actions align with established policies on Auditing and Accountability, System and Information Integrity, Computer Security Threat Response, and Planning.

### RESPOND

**Section: Respond Function of the NIST Cybersecurity Framework**

The organization shall establish and execute its incident response plan in coordination with relevant third parties (RS.MA-01) upon the declaration of an incident. Incident reports shall be triaged and validated (RS.MA-02), and incidents shall be categorized and prioritized (RS.MA-03). Escalation or elevation of incidents shall occur as necessary (RS.MA-04). The criteria for initiating incident recovery shall be applied (RS.MA-05).

Internal and external stakeholders shall be notified of incidents, and information shared with designated parties shall be consistent with response plans (RS.CO-02 & RS.CO-03). Root cause analysis shall be performed to establish what has taken place during an incident (RS.AN-03). The organization shall monitor its systems for potentially adverse events (implied by NIST Function: Detect) and utilize approved methods and messaging to communicate recovery criteria.

### RECOVER

Policy Section: Recovery - Incident Recovery Plan Execution (RC.RP)

The organization shall execute the recovery portion of the incident response plan once initiated from the incident response process (RC.RP-01). The recovery actions shall be selected, scoped, prioritized, and performed (RC.RP-02). Prior to using backups and other restoration assets, their integrity must be verified (RC.RP-03). Critical mission functions and cybersecurity risk management considerations shall be integrated to establish post-incident operational norms (RC.RP-04). The organization shall verify the integrity of restored assets, restore systems and services, and confirm normal operating status (RC.RP-05). The end of incident recovery shall be declared based on established criteria, and related documentation shall be completed (RC.RP-06).

Recovery activities and progress in restoring operational capabilities shall be communicated to designated internal and external stakeholders (RC.CO-03). Public updates on incident recovery shall be shared using approved methods and messaging (RC.CO-04).
