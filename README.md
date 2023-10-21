# Container Security SBOM Analysis

Containerization has become a widely adopted approach for running contemporary software services, with its ingenious layering of Free Open Source Software <strong>FOSS</strong> libraries and packages. The security of containers heavily relies on the integrity of their underlying dependencies, making vulnerability assessment a critical focus for security professionals. However, the landscape has evolved, and recent software supply chain attacks have illuminated a pressing need to shift the focus beyond individual vulnerabilities and delve into the overall security of their supply chain. In this paper, we embark on a data-driven analysis of container threats by examining the security characteristics of software supply chains in their open source dependencies. Leveraging a comprehensive dataset of containers from Docker Hub, our study employs Software Supply Chain metrics like the OSSF scorecard and Software Bill of Material <strong>SBOM</strong> tooling to compile dependency lists. The analysis delivers valuable insights to the security community, empowering them to adopt more effective measures in thwarting and mitigating software supply chain attacks, thereby enhancing the resilience of modern software services.

## Data decsription
 - Compiled list of Docker image names from both official and unofficial (i.e. community) containers available on DockerHub. (https://github.com/Motahareee/sinconf23_sbom/blob/main/Data/uniqueSearchFrom1to3.csv)
- *unique_dependencies.csv* contains name of all the dependencies listed for the collected docker images.


Please cite this data as follows[^1]:
[^1]: M. Mounesan, H. Siadati and S. Jafarikhah, "Exploring the Threat of Software Supply Chain Attacks on Containerized Applications," in International Conference on Security of Information and Networks (SINCONF), 2023, [https://www.researchgate.net/publication/374838986_Exploring_the_Threat_of_Software_Supply_Chain_Attacks_on_Containerized_Applications#fullTextFileContent]
