# GapBridge Policy Gap Analysis Report

**Overall Maturity Score:** 21.7% (Basic)
**Weighted Score:** 18.0%

## Scorecard by NIST Function

- **GOVERN:** 19/31 controls met (61.3%)
- **IDENTIFY:** 1/21 controls met (4.8%)
- **PROTECT:** 2/22 controls met (9.1%)
- **DETECT:** 0/11 controls met (0.0%)
- **RESPOND:** 0/13 controls met (0.0%)
- **RECOVER:** 1/8 controls met (12.5%)

## Recommendations

### IDENTIFY (4.8% - needs attention)

1. Establish an Asset Management Policy that includes maintaining inventories of hardware (ID.AM-1), software (ID.AM-2), and services (ID.AM-4) to have a comprehensive view of the organization's IT assets.

2. Implement a network discovery tool for mapping internal and external communication and data flows (ID.AM-3) to identify all connected devices, applications, and services within the organization's network.

3. Adopt a Vulnerability Management Program to proactively identify, validate, and record vulnerabilities in assets (ID.RA-01), ensuring regular scans to minimize security risks and improve overall cybersecurity posture.

### PROTECT (9.1% - needs attention)

1. Implement a robust identity and access management system to address PR.AA-01, PR.AA-03, and PR.AA-05. This system should enforce least privilege principles, separate duties, and manage access permissions effectively.

2. To secure data at rest (PR.DS-01) and in transit (PR.DS-02), consider deploying encryption solutions for all sensitive information across the organization's hardware and software infrastructure.

3. Regularly conduct training sessions (PR.AT-02) to educate users about cybersecurity risks, best practices, and secure authentication methods to minimize security vulnerabilities associated with human error.

### DETECT (0.0% - needs attention)

1. Implement a Security Information and Event Management (SIEM) solution to correlate information from multiple sources across the organization, addressing DE.AE-03 and DE.CM-01.

2. Conduct regular threat hunting exercises to analyze potentially adverse events, understanding their associated activities and estimated impact, in accordance with DE.AE-02 and DE.AE-04.

3. Develop clear incident criteria that trigger an incident declaration, ensuring authorized staff and tools are promptly informed of adverse events when they occur, addressing DE.AE-08 and DE.AE-06.

### RESPOND (0.0% - needs attention)

1. Develop and formalize a process to collaborate with relevant third parties in executing the incident response plan (RS.MA-01).
2. Implement a triage system for validating incident reports and prioritizing them based on severity (RS.MA-02, RS.MA-03).
3. Establish clear criteria for escalating or elevating incidents and initiating recovery procedures (RS.MA-04, RS.MA-05). Additionally, create a communication plan to notify internal and external stakeholders of incidents and to share information with them consistently (RS.CO-02, RS.CO-03).
4. Implement an incident analysis process to determine the root cause of incidents (RS.AN-03) as part of the ongoing effort to improve the organization's response capabilities.

### RECOVER (12.5% - needs attention)

1. Develop an incident response plan that clearly outlines the steps to execute RC.RP-01 and RC.RP-02, including the selection, prioritization, and execution of recovery actions once initiated from the incident response process.

2. Implement a backup verification system in accordance with RC.RP-03 to ensure the integrity of backups and other restoration assets before they are used for restoration, reducing the risk of data loss or corruption during recovery.

3. Establish clear criteria for declaring the end of an incident recovery in line with RC.RP-06 and RC.CO-06, while also creating a communication plan to keep internal and external stakeholders informed of recovery progress (RC.CO-03) and provide public updates using approved methods and messaging (RC.CO-04).


## Appendix: Full Gap Details

- **GV.OC-01** [GOVERN] Met (score: 0.56) - The organizational mission is understood and informs cybersecurity risk management
- **GV.OC-02** [GOVERN] Met (score: 0.52) - Internal and external stakeholders are understood, and their needs and expectations regarding cybersecurity risk management are understood and considered
- **GV.OC-03** [GOVERN] Met (score: 0.5) - Legal, regulatory, and contractual requirements regarding cybersecurity, including privacy and civil liberties obligations, are understood and managed
- **GV.OC-04** [GOVERN] Gap (score: 0.28) - Critical objectives, capabilities, and services that stakeholders depend on or expect from the organization are understood and communicated
- **GV.OC-05** [GOVERN] Gap (score: 0.25) - Outcomes, capabilities, and services that the organization depends on are understood and communicated
- **GV.RM-01** [GOVERN] Met (score: 0.59) - Risk management objectives are established and agreed to by organizational stakeholders
- **GV.RM-02** [GOVERN] Gap (score: 0.34) - Risk appetite and risk tolerance statements are established, communicated, and maintained
- **GV.RM-03** [GOVERN] Met (score: 0.59) - Cybersecurity risk management activities and outcomes are included in enterprise risk management processes
- **GV.RM-04** [GOVERN] Gap (score: 0.41) - Strategic direction that describes appropriate risk response options is established and communicated
- **GV.RM-05** [GOVERN] Met (score: 0.49) - Lines of communication across the organization are established for cybersecurity risks, including risks from suppliers and other third parties
- **GV.RM-06** [GOVERN] Met (score: 0.52) - A standardized method for calculating, documenting, categorizing, and prioritizing cybersecurity risks is established and communicated
- **GV.RM-07** [GOVERN] Met (score: 0.49) - Strategic opportunities (i.e., positive risks) are characterized and are included in organizational cybersecurity risk discussions
- **GV.RR-01** [GOVERN] Met (score: 0.49) - Organizational leadership is responsible and accountable for cybersecurity risk and fosters a culture that is risk-aware, ethical, and continually improving
- **GV.RR-02** [GOVERN] Met (score: 0.61) - Roles, responsibilities, and authorities related to cybersecurity risk management are established, communicated, understood, and enforced
- **GV.RR-03** [GOVERN] Met (score: 0.49) - Adequate resources are allocated commensurate with the cybersecurity risk strategy, roles, responsibilities, and policies
- **GV.RR-04** [GOVERN] Gap (score: 0.39) - Cybersecurity is included in human resources practices
- **GV.PO-01** [GOVERN] Met (score: 0.7) - Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced
- **GV.PO-02** [GOVERN] Met (score: 0.7) - Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced to reflect changes in requirements, threats, technology, and organizational mission
- **GV.OV-01** [GOVERN] Met (score: 0.54) - Cybersecurity risk management strategy outcomes are reviewed to inform and adjust strategy and direction
- **GV.OV-02** [GOVERN] Met (score: 0.66) - The cybersecurity risk management strategy is reviewed and adjusted to ensure coverage of organizational requirements and risks
- **GV.OV-03** [GOVERN] Met (score: 0.56) - Organizational cybersecurity risk management performance is evaluated and reviewed for adjustments needed
- **GV.SC-01** [GOVERN] Met (score: 0.5) - A cybersecurity supply chain risk management program, strategy, objectives, policies, and processes are established and agreed to by organizational stakeholders
- **GV.SC-02** [GOVERN] Gap (score: 0.35) - Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally
- **GV.SC-03** [GOVERN] Met (score: 0.45) - Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes
- **GV.SC-04** [GOVERN] Gap (score: 0.15) - Suppliers are known and prioritized by criticality
- **GV.SC-05** [GOVERN] Gap (score: 0.41) - Requirements to address cybersecurity risks in supply chains are established, prioritized, and integrated into contracts and other types of agreements with suppliers and other relevant third parties
- **GV.SC-06** [GOVERN] Gap (score: 0.27) - Planning and due diligence are performed to reduce risks before entering into formal supplier or other third-party relationships
- **GV.SC-07** [GOVERN] Gap (score: 0.34) - The risks posed by a supplier, their products and services, and other third parties are understood, recorded, prioritized, assessed, responded to, and monitored over the course of the relationship
- **GV.SC-08** [GOVERN] Gap (score: 0.22) - Relevant suppliers and other third parties are included in incident planning, response, and recovery activities
- **GV.SC-09** [GOVERN] Gap (score: 0.45) - Supply chain security practices are integrated into cybersecurity and enterprise risk management programs, and their performance is monitored throughout the technology product and service life cycle
- **GV.SC-10** [GOVERN] Met (score: 0.45) - Cybersecurity supply chain risk management plans include provisions for activities that occur after the conclusion of a partnership or service agreement
- **ID.AM-1** [IDENTIFY] Gap (score: 0.23) - Inventories of hardware managed by the organization are maintained
- **ID.AM-2** [IDENTIFY] Gap (score: 0.23) - Inventories of software, services, and systems managed by the organization are maintained
- **ID.AM-3** [IDENTIFY] Gap (score: 0.34) - Representations of the organization's authorized network communication and internal and external network data flows are maintained
- **ID.AM-4** [IDENTIFY] Gap (score: 0.12) - Inventories of services provided by suppliers are maintained
- **ID.AM-5** [IDENTIFY] Gap (score: 0.18) - Assets are prioritized based on classification, criticality, resources, and impact on the mission
- **ID.AM-7** [IDENTIFY] Gap (score: 0.18) - Inventories of data and corresponding metadata for designated data types are maintained
- **ID.AM-8** [IDENTIFY] Gap (score: 0.22) - Systems, hardware, software, services, and data are managed throughout their life cycles
- **ID.RA-01** [IDENTIFY] Gap (score: 0.31) - Vulnerabilities in assets are identified, validated, and recorded
- **ID.RA-02** [IDENTIFY] Gap (score: 0.38) - Cyber threat intelligence is received from information sharing forums and sources
- **ID.RA-03** [IDENTIFY] Gap (score: 0.33) - Internal and external threats to the organization are identified and recorded
- **ID.RA-04** [IDENTIFY] Gap (score: 0.4) - Potential impacts and likelihoods of threats exploiting vulnerabilities are identified and recorded
- **ID.RA-05** [IDENTIFY] Met (score: 0.53) - Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization
- **ID.RA-06** [IDENTIFY] Gap (score: 0.43) - Risk responses are chosen, prioritized, planned, tracked, and communicated
- **ID.RA-07** [IDENTIFY] Gap (score: 0.39) - Changes and exceptions are managed, assessed for risk impact, recorded, and tracked
- **ID.RA-08** [IDENTIFY] Gap (score: 0.34) - Processes for receiving, analyzing, and responding to vulnerability disclosures are established
- **ID.RA-09** [IDENTIFY] Gap (score: 0.17) - The authenticity and integrity of hardware and software are assessed prior to acquisition and use
- **ID.RA-10** [IDENTIFY] Gap (score: 0.1) - Critical suppliers are assessed prior to acquisition
- **ID.IM-01** [IDENTIFY] Gap (score: 0.05) - Improvements are identified from evaluations
- **ID.IM-02** [IDENTIFY] Gap (score: 0.28) - Improvements are identified from security tests and exercises, including those done in coordination with suppliers and relevant third parties
- **ID.IM-03** [IDENTIFY] Gap (score: 0.12) - Improvements are identified from execution of operational processes, procedures, and activities
- **ID.IM-04** [IDENTIFY] Gap (score: 0.45) - Incident response plans and other cybersecurity plans that affect operations are established, communicated, maintained, and improved
- **PR.AA-01** [PROTECT] Gap (score: 0.41) - Identities and credentials for authorized users, services, and hardware are managed by the organization
- **PR.AA-02** [PROTECT] Gap (score: 0.23) - Identities are proofed and bound to credentials based on the context of interactions
- **PR.AA-03** [PROTECT] Gap (score: 0.25) - Users, services, and hardware are authenticated
- **PR.AA-04** [PROTECT] Gap (score: 0.26) - Identity assertions are protected, conveyed, and verified
- **PR.AA-05** [PROTECT] Gap (score: 0.43) - Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed, and incorporate the principles of least privilege and separation of duties
- **PR.AA-06** [PROTECT] Met (score: 0.47) - Physical access to assets is managed, monitored, and enforced commensurate with risk
- **PR.AT-01** [PROTECT] Met (score: 0.46) - Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with cybersecurity risks in mind
- **PR.AT-02** [PROTECT] Gap (score: 0.37) - Individuals in specialized roles are provided with awareness and training so that they possess the knowledge and skills to perform relevant tasks with cybersecurity risks in mind
- **PR.DS-01** [PROTECT] Gap (score: 0.28) - The confidentiality, integrity, and availability of data-at-rest are protected
- **PR.DS-02** [PROTECT] Gap (score: 0.32) - The confidentiality, integrity, and availability of data-in-transit are protected
- **PR.DS-10** [PROTECT] Gap (score: 0.43) - The confidentiality, integrity, and availability of data-in-use are protected
- **PR.DS-11** [PROTECT] Gap (score: 0.43) - The confidentiality, integrity, and availability of data-in-use are protected
- **PR.PS-01** [PROTECT] Gap (score: 0.41) - Configuration management practices are established and applied
- **PR.PS-02** [PROTECT] Gap (score: 0.28) - Software is maintained, replaced, and removed commensurate with risk
- **PR.PS-03** [PROTECT] Gap (score: 0.25) - Hardware is maintained, replaced, and removed commensurate with risk
- **PR.PS-04** [PROTECT] Gap (score: 0.14) - Log records are generated and made available for continuous monitoring
- **PR.PS-05** [PROTECT] Gap (score: 0.19) - Installation and execution of unauthorized software are prevented
- **PR.PS-06** [PROTECT] Gap (score: 0.4) - Secure software development practices are integrated, and their performance is monitored throughout the software development life cycle
- **PR.IR-01** [PROTECT] Gap (score: 0.36) - Networks and environments are protected from unauthorized logical access and usage
- **PR.IR-02** [PROTECT] Gap (score: 0.43) - The organization's technology assets are protected from environmental threats
- **PR.IR-03** [PROTECT] Gap (score: 0.27) - Mechanisms are implemented to achieve resilience requirements in normal and adverse situations
- **PR.IR-04** [PROTECT] Gap (score: 0.15) - Adequate resource capacity to ensure availability is maintained
- **DE.AE-02** [DETECT] Gap (score: 0.25) - Potentially adverse events are analyzed to better understand associated activities
- **DE.AE-03** [DETECT] Gap (score: 0.09) - Information is correlated from multiple sources
- **DE.AE-04** [DETECT] Gap (score: 0.27) - The estimated impact and scope of adverse events are understood
- **DE.AE-06** [DETECT] Gap (score: 0.36) - Information on adverse events is provided to authorized staff and tools
- **DE.AE-07** [DETECT] Gap (score: 0.4) - Cyber threat intelligence and other contextual information are integrated into the analysis
- **DE.AE-08** [DETECT] Gap (score: 0.29) - Incidents are declared when adverse events meet the defined incident criteria
- **DE.CM-01** [DETECT] Gap (score: 0.29) - Networks and network services are monitored to find potentially adverse events
- **DE.CM-02** [DETECT] Gap (score: 0.25) - The physical environment is monitored to find potentially adverse events
- **DE.CM-03** [DETECT] Gap (score: 0.4) - Personnel activity and technology usage are monitored to find potentially adverse events
- **DE.CM-06** [DETECT] Gap (score: 0.25) - External service provider activities and services are monitored to find potentially adverse events
- **DE.CM-09** [DETECT] Gap (score: 0.3) - Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events
- **RS.MA-01** [RESPOND] Gap (score: 0.27) - The incident response plan is executed in coordination with relevant third parties once an incident is declared
- **RS.MA-02** [RESPOND] Gap (score: 0.2) - Incident reports are triaged and validated
- **RS.MA-03** [RESPOND] Gap (score: 0.27) - Incidents are categorized and prioritized
- **RS.MA-04** [RESPOND] Gap (score: 0.22) - Incidents are escalated or elevated as needed
- **RS.MA-05** [RESPOND] Gap (score: 0.17) - The criteria for initiating incident recovery are applied
- **RS.CO-02** [RESPOND] Gap (score: 0.22) - Internal and external stakeholders are notified of incidents
- **RS.CO-03** [RESPOND] Gap (score: 0.29) - Information is shared with designated internal and external stakeholders, consistent with response plans
- **RS.AN-03** [RESPOND] Gap (score: 0.2) - Analysis is performed to establish what has taken place during an incident and the root cause of the incident
- **RS.AN-06** [RESPOND] Gap (score: 0.13) - Actions performed during an investigation are recorded, and the records' integrity and provenance are preserved
- **RS.AN-07** [RESPOND] Gap (score: 0.16) - Incident data and metadata are collected, and their integrity and provenance are preserved
- **RS.AN-08** [RESPOND] Gap (score: 0.16) - An incident's magnitude is estimated and validated
- **RS.MI-01** [RESPOND] Gap (score: 0.19) - Incidents are contained
- **RS.MI-02** [RESPOND] Gap (score: 0.1) - Incidents are eradicated
- **RC.RP-01** [RECOVER] Gap (score: 0.2) - The recovery portion of the incident response plan is executed once initiated from the incident response process
- **RC.RP-02** [RECOVER] Gap (score: 0.2) - Recovery actions are selected, scoped, prioritized, and performed
- **RC.RP-03** [RECOVER] Gap (score: 0.07) - The integrity of backups and other restoration assets is verified before using them for restoration
- **RC.RP-04** [RECOVER] Met (score: 0.45) - Critical mission functions and cybersecurity risk management are considered to establish post-incident operational norms
- **RC.RP-05** [RECOVER] Gap (score: 0.12) - The integrity of restored assets is verified, systems and services are restored, and normal operating status is confirmed
- **RC.RP-06** [RECOVER] Gap (score: 0.17) - The end of incident recovery is declared based on criteria, and incident-related documentation is completed
- **RC.CO-03** [RECOVER] Gap (score: 0.2) - Recovery activities and progress in restoring operational capabilities are communicated to designated internal and external stakeholders
- **RC.CO-04** [RECOVER] Gap (score: 0.19) - Public updates on incident recovery are shared using approved methods and messaging