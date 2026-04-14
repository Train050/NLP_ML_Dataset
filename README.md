# CAP6640 Final Project investigating LLM accuracy on fixing real-world bugs

## 1 . Data Description

- CVE entries in our dataset cover the period from 2002 to 2019, each consisting of 21 features. Each feature's name and corresponding column name in the CSV file are explained in the following table. The dataset is released as comma-separated values(CSV) format ([all_c_cpp_release2.0.csv](https://github.com/ZeoVan/MSR_20_Code_Vulnerability_CSV_Dataset/blob/master/all_c_cpp_release2.0.csv)).

|           Features           |    Column Name in the CSV     |                         Description                          |
| :--------------------------: | :---------------------------: | :----------------------------------------------------------: |
|      Access Complexity       |      access\_complexity       | Reflects the complexity of the attack required to exploit the software feature misuse vulnerability |
|   Authentication Required    |   authentication\_required    |  If authentication is required to exploit the vulnerability  |
|     Availability Impact      |     availability\_impact      | Measures the potential impact to availability of a successfully exploited misuse vulnerability |
|          Commit ID           |          commit\_id           |   Commit ID in code repository, indicating a mini-version    |
|        Commit Message        |        commit\_message        |                Commit message from developer                 |
|    Confidentiality Impact    |    confidentiality\_impact    | Measures the potential impact on confidentiality of a successfully exploited misuse vulnerability |
|            CWE ID            |            cwe\_id            |                Common Weakness Enumeration ID                |
|            CVE ID            |            cve\_id            |           Common Vulnerabilities and Exposures ID            |
|           CVE Page           |           cve\_page           |            CVE Details web page link for that CVE            |
|         CVE Summary          |            summary            |                   CVE summary information                    |
|          CVSS Score          |             score             |    The relative severity of software flaw vulnerabilities    |
|        Files Changed         |        files\_changed         |       All the changed files and corresponding patches        |
|       Integrity Impact       |       integrity\_impact       | Measures the potential impact to integrity of a successfully exploited misuse vulnerability\ |
|    Mini-version After Fix    |      version\_after\_fix      |                Mini-version ID after the fix                 |
|   Mini-version Before Fix    |     version\_before\_fix      |                Mini-version ID before the fix                |
|     Programming Language     |             lang              |                 Project programming language                 |
|           Project            |            project            |                         Project name                         |
|         Publish Date         |         publish\_date         |                   Publish date of the CVE                    |
|        Reference Link        |           ref\_ink            |                Reference link in the CVE page                |
|         Update Date          |         update\_date          |                    Update date of the CVE                    |
| Vulnerability Classification | vulnerability\_classification |                      Vulnerability type                      |

- The cleaned version of split functions(CSV format) can be found at: https://drive.google.com/file/d/1-0VhnHBp9IGh90s2wCNjeCMuy70HPl8X/view?usp=sharing  

  Some of the intermediary files in the data collecting and cleaning process can be found at:https://drive.google.com/file/d/1E95oVDSO0CfAAs-Q0yav2HBGLZQce_v2/view?usp=sharing
  
  Also JSON format dataset can be found at: https://drive.google.com/file/d/1deNsPfeh77h1SHjJURYOeyCR96JgxB_A/view?usp=sharing
  
  - Split functions are released as comma-separated values(CSV) format:
  
  | Column Name in the CSV |                         Description                          |
  | :--------------------: | :----------------------------------------------------------: |
  |      func_before       | The function before the vulnerability being fixed(if "vul" labeled as "1", then this is the vulnerable function) |
  |       func_after       |       The function after the vulnerability being fixed       |
  |      lines_before      | The modified lines in the founction before the vulnerability being fixed |
  |      lines_after       | The modified lines in the founction after the vulnerability being fixed |
  |          vul           | "1" means vulnerable function and "0" means non-vulnerable function |
  |   vul_func_with_fix    |  The code comments showing how the vulnerability was fixed   |

  - only_vulnerability.csv is the same as MSR_data_cleaned, being a comma-separated value(CSV) file, but only includes entries that have bugs.

  - llmResponses is in comma-separated values(CSV) format:

  | Column Name in the CSV |                         Description                          |
  | :--------------------: | :----------------------------------------------------------: |
  |      llmModel         | The LLM model that produced the bug-free version of code      |
  |      execTime         | The time that the LLM took to output its bug-free solution    |
  |      programLang      |                  Code programming language                    |
  |      vulnType         |                      Vulnerability type                       |
  |      vulnSeverity     | The relative severity of software flaw vulnerabilities        |
  |      iteration        |       Which bug-filled code snippet was originally supplied to the model. |
  |      llmFixCode       | The LLM output that intended to fix the buggy code            |
  |      csvFixCode       | The function after the vulnerability being fixed              |

  - llmScores is in comma-separated values(CSV) format:
  
  | Column Name in the CSV |                         Description                          |
  | :--------------------: | :----------------------------------------------------------: |
  |      llmModel         | The LLM model that produced the bug-free version of code      |
  |      execTime         | The time that the LLM took to output its bug-free solution    |
  |      programLang      |                  Code programming language                    |
  |      vulnType         |                      Vulnerability type                       |
  |      vulnSeverity     | The relative severity of software flaw vulnerabilities        |
  |      iteration        |       Which bug-filled code snippet was originally supplied to the model. |
  |      llmFixCode       | The LLM output that intended to fix the buggy code            |
  |      csvFixCode       | The function after the vulnerability being fixed              |
  |       score           |       The score that deepseek identified and extracted for the model,                |
  |                       |       with 30 points from identifying the bug and 70 points from fixing it correctly.|

  - Only Score Column is in comma-separated values(CSV) format:

  | Column Name in the CSV |                         Description                          |
  | :--------------------: | :----------------------------------------------------------: |
  |      llmModel         | The LLM model that produced the bug-free version of code      |
  |       iteration       |       Which bug-filled code snippet was originally supplied to the model.            |
  |       score           |       The score that deepseek identified and extracted for the model,                |
  |                       |       with 30 points from identifying the bug and 70 points from fixing it correctly.|

## 2. HOW To Use The Scripts

- Pre-Requirements
  - [Python3](https://www.linuxbabe.com/ubuntu/install-python-3-6-ubuntu-16-04-16-10-17-04)
  
  - How to use
    - First use [get_vuln_code.py] to extract the code snippets from the [MSR_data_cleaned.csv] file that contain bugs ([MSR_data_cleaned.csv] can be obtained from the google doc link above, and should be placed within the [MSR_data_cleaned] folder). The output file will be named [only-vulnerability.csv]
    - Then, run [runModel.py] to run each of the 3 LLMs, qwen 2.5, Llama 3.2, and Gemma 4, on the bug-filled code snippets. Their results will be saved under the [llmResponses] folder, with each LLM being saved to a seperate CSV corresponding to their name.
    - After that, you run [codeScorer.py], which will use deepseek-r1 to score each of the proposed code corrections with the code that was implemented in the real-world code input. The score produces is out of 100 points, with 30 points being added if the LLM found the bug correctly and 70 points for matching the functionality of the provided fix. The code will output corresponding named .csv files to the [llmScores] folder.
    - Lastly, you run [findScores.py] to extract only the score from each of the [llmScore] csv files for each of the LLMs. Despite a clear prompt being provided, deepseek did
    not always respond in the requested format, so it has to go back through the results and extract the correct score from the end of each line.
  
  ## Citation
  
  ACM Reference Format:
  
  Jiahao Fan, Yi Li, Shaohua Wang and Tien N. Nguyen. 2020. A C/C++ Code Vulnerability Dataset with Code Changes and CVE Summaries. In MSR ’20: The 17th International Conference on Mining Software Repositories,May 25–26, 2020, MSR, Seoul, South Korea. ACM, New York, NY, USA, 5 pages. https://doi.org/10.1145/3379597.3387501
