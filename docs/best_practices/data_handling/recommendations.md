---
title: "C2SM Data Management Recommendations"
---

# C2SM Data Management Recommendations

R. Lorenz<sup>1</sup>, U. Beyerle<sup>1</sup>, I. Iosifescu Enescu<sup>3</sup>, S. Ferrachat<sup>1</sup>, M. Hauser<sup>1</sup>, M. Hirschi<sup>1</sup>, S. Henne<sup>2</sup>, M. Jähn<sup>1</sup>, M. Münnich<sup>1</sup>, G.-K. Plattner<sup>3</sup>, C. Schnadt Poberaj<sup>1</sup>, M. Sprenger<sup>1</sup>

<sup>1</sup> Swiss Federal Institute of Technology ETH,
<sup>2</sup> Swiss Federal Laboratories for Materials Science and Technology Empa,
<sup>3</sup> Swiss Federal Institute for Forest, Snow and Landscape Research WSL

<button class="md-button print-button" onclick="window.print()">Download PDF</button>

## 1. Introduction

These guidelines are primarily recommendations to research staff of the
C2SM community at ETH Zurich, since Empa, Eawag, MeteoSwiss and WSL have
their own guidelines. We aim to complement the
[Guidelines for Research Data Management at ETH Zurich :material-open-in-new:](https://ethz.ch/content/dam/ethz/main/eth-zurich/organisation/rechtssammlung/414.2en.pdf){:target="_blank"}
with more specific recommendations for climate scientists from the
Master level all across to senior scientists how to organise, manage,
and document their research data, and where and how to store these data
at suitable repositories. The recommendations focus on large data sets
typically produced from weather and climate models, but are applicable
to other types of data as well.
<!-- TODO: Add link to further recommendations regarding very large
datasets from high resolution kilometer-scale climate model simulations. -->

All data must be managed according to the international FAIR principles
(Findable, Accessible, Interoperable, and Reusable) and the ideal of
Open Research Data (ORD). Meaning data should be *"as open as possible,
as closed as necessary."*

General information on research data management is also available from
the [ETH library :material-open-in-new:](https://library.ethz.ch/en/researching-and-publishing/data-management-and-policies.html){:target="_blank"}.
Legal aspects are covered by the
[ETH Guidelines for Research Integrity :material-open-in-new:](https://doi.org/10.3929/ethz-b-000179298){:target="_blank"},
which have been developed by
[ETH commission of Good Scientific Practice (GSP) :material-open-in-new:](https://ethz.ch/en/the-eth-zurich/organisation/boards-university-groups-commissions/commission-gsp.html){:target="_blank"}.
Articles 11 and 12 in the latter guidelines explicitly regulate the
rights and obligations of ETH researchers concerning the collection,
documentation, and storage of primary data, as well as the rights to the
primary data and materials. Importantly, data is owned by the respective
institution and remains with ETH even if researchers leave ETH. WSL
researchers should also consult the WSL Compliance Guide (available in
WSL-Intranet), especially the section on Research Data Management (RDM)
and Open Research Data (ORD).

The division of data management responsibilities is a balance between
governance and execution. The Principal Investigator (PI) holds ultimate
institutional and legal accountability, focusing on establishing the
group's overarching data strategy, ensuring compliance with
institutional and funder mandates, and overseeing long-term data
continuity. In contrast, the PhD students and PostDocs handle the daily,
hands-on implementation. They actively maintain their specific
project's Data Management Plan (DMP), ensuring precise documentation
and secure storage, and executing a complete data handover prior to
leaving to satisfy the mandatory 10-year retention rule. Data users must
treat existing datasets with academic rigor by providing proper
citations and adhering strictly to all legal, ethical, licensing and
export restrictions. Additionally, they are responsible for
transparently documenting any modifications or analyses performed on the
data to maintain scientific integrity and reproducibility.

These guidelines are under continuous development. We very much
appreciate feedback of any kind (gaps, inconsistencies, suggested
additions, etc.) to <support@c2sm.ethz.ch>.

## 2. Research data definitions

The term *research data* not only refers to numerical datasets, but to
all kinds of information that can be used to reproduce, validate, or
re-use scientific work. We will use the term *data package* in order to
describe the research data used for a specific project or a publication.

### 2.1 Primary data

Strictly speaking, primary data is digital data that is the direct
result of simulations or measurements, hence the original unanalysed
data collected from experiments or other sources. In practice however, a
modified form of that data, e.g. through averaging or the discarding of
irrelevant data, is frequently considered primary data. As a rule of
thumb, primary data is data for which there exists no previous
incarnation. The researcher, considering conventions in her or his
field, defines what exactly to archive as primary data.

> **Primary data examples:** Weather and climate model simulations,
> reanalysis data sets, measurements from field instruments, etc.
> Remember that the user has to decide him/herself what exactly has to
> be declared as primary data.

#### 2.1.1 Raw data

Raw data can be defined as data that has not been processed,
transformed, or analyzed since its initial collection from a physical
source. Under ETH Zurich guidelines, raw data represents the absolute
starting point of the empirical data lifecycle. It is the direct output
from observational platforms, sensors, or field instruments before any
quality control, calibration equations, or physical unit conversions are
applied. Because physical observations cannot be replicated if the
original source files are lost, archiving raw data (alongside its
metadata) is critical for long-term data provenance.

- **Raw data examples:** Raw voltage signals or unprocessed,
  high-frequency digital data from eddy covariance towers, output
  retrieved from field data loggers, uncalibrated digital counts from
  satellite sensors, raw binary data from weather radars, or handwritten
  field logs.

- **Storage Recommendation:** Raw data must **never** be stored
  exclusively on local hard drives or instrument laptops. During active
  research, it must be stored on secure, redundant network storage
  provided by your departmental IT Service Group (ISG) or central IT
  Services (e.g., central NAS or replicated S3 buckets) of your
  institution. For the mandatory 10-year preservation phase, raw
  datasets must be archived using the ETH Library's institutional
  repository (ETH Research Collection), which automatically pushes data
  to the geo-redundant ETH Data Archive for long-term preservation.

#### 2.1.2 Original simulation output

While often categorized broadly as primary data, original simulation
output must be distinguished from observational raw data. It refers to
the immediate, un-postprocessed digital files generated directly by a
numerical weather prediction (NWP) or climate model run. This data is in
its native grid and time step, containing all prognostic variables
before any spatial interpolation, temporal averaging (e.g., monthly
means), or diagnostic variable calculations occur.

- **Original simulation output examples:** Raw history or restart files
  directly from an atmospheric/oceanic general circulation model (GCM),
  or native-grid output from a high-resolution regional climate model
  (RCM).

- **Storage Recommendation:** Active simulation runs are typically
  generated on high-performance computing (HPC) scratch spaces. Because
  scratch space is not backed up and is subject to automated purging,
  critical outputs must be moved immediately upon run completion. Due to
  the massive volume of climate files, storing all original output on
  standard redundant disk storage is often financially or technically
  unfeasible. In alignment with Art. 5 of the ETH RDM Guidelines, if the
  data is too large for standard redundant storage, the researcher must
  secure the exact code version (e.g., on gitlab.ethz.ch), namelists,
  seeding keys, and boundary conditions required to deterministically
  *recreate* the simulation. If the native files themselves are
  irreplaceable, they must be moved to Tape-Based Long-Term Storage
  (LTS) provided by ETH IT Services or CSCS.

### 2.2 Derived data

In addition to the primary data, for a data package you should include
as a minimum all datasets necessary to reproduce the figures, tables,
and individual numbers in the running text that are presented in the
main paper and the supporting information. In case you decide to delete
some of your primary data, archiving derived data is essential.

> **Derived data examples**: Weather feature climatologies, trend
> analyses, etc. These data are produced from the primary data using
> programs and scripts (Fortran, Shell scripts, Python, R, Matlab, NCL,
> etc.)

#### 2.2.1 Processed data

Processed data refers to data which was processed in a certain way, for
example averaging over certain time periods, like calculating monthly
averages from daily values. For reproducability it is important to note
which scripts or version of code were used to process the data.

### 2.3 Curated data

Curated data is organized, cleaned, enriched, and documented to make it
highly accurate, accessible, and ready for use. Unlike raw data, which
can be chaotic and fragmented, curated data is actively managed
throughout its lifecycle to ensure long-term value and trustworthiness.
The CMIP6-next generation archive is an example of curated data at C2SM
([Brunner et al. 2020 :material-open-in-new:](https://zenodo.org/records/3734128){:target="_blank"}).

### 2.4 Published data

Published data is a selected subset of data for a selected publication,
published in a data repository such as the ETH Research Collection or
WSL's environmenral data portal EnviDat. We will use the term *data
package* in order to describe the research data used for a specific
project or a publication.

The data in the package needs to be annotated to be useful for other
researchers or your future self. Each package should contain a README -
file that describes the package at the highest level. The README file

- is a pure ASCII or UTF-8 text-file (README.txt) or is written in a
  common markup-language such as
  [Markdown :material-open-in-new:](https://en.wikipedia.org/wiki/Markdown){:target="_blank"}
  (README.md), or HTML (README.html).

- has an understandable description of the dataset explaining what are
  the research data files about and a brief summary of the methods used
  to obtain them

- has to reference, implicitly or explicitly, each other file in the
  package and thus can be used to look up the purpose and description of
  each element of the project.

- describes the project structure, that is the organisation in a
  [folder-hierarchy :material-open-in-new:](https://opendata.eawag.ch/docs/research-data-management/archiving-guide.html#folder-structure-and-file-archives){:target="_blank"}
  (if there is one) and the [file-naming :material-open-in-new:](https://opendata.eawag.ch/docs/research-data-management/archiving-guide.html#file-naming){:target="_blank"}
  convention used, if applicable.

- should mention if the package contains files in a non-common format
  and point to required software to read them.

- should contain all information necessary to interpret and understand
  the dataset that is not recorded elsewhere, e.g., meaning of column
  headers, abbreviations, units of variables, etc.

- should contain pointers to other files in the package that contain
  scientific metadata.

- should contain a reference to the associated article or report (as a
  [DOI :material-open-in-new:](https://www.doi.org/){:target="_blank"} if possible), if applicable.

#### 2.4.1 Ancillary information

Generously add any files and information to your data package that could
further help to understand your work or build on your results. This
includes, for example, photos and figures of a related publication and
its supporting information, maps, pointers to related resources such as
the project website, etc.

> **Examples:** Written report or presentation, paper, thesis. The
> report is created based on the processed data (Word, LaTeX,
> Powerpoint, visualisation software).

### 2.5 Third-party data

Third-party data is data used for research, but which has not been
created within the frame of the respective research project. It is
important to properly document the origin of this data and, e.g., when
the data was downloaded, because many datasets may exist in different
versions. Be aware whether there are restrictions to publish or pass on
this third party data. Do not upload restricted third party data
together with your data in a research data publication repository, but
rather explain what third-party data has been used and how other users
can obtain it again from the original source.

## 3. Software related definitions

A lot of software is used in research and data management and can have
different forms. Software can be available in source code or as
proprietary software. For reproducibility purposes, it is crucial to
know which version of software was used to create or process a dataset.
Reproducibility means the ability to consistently achieve the exact same
output, results, or behavior when running the same software on the same
input data. Please check licenses of all software used so it does not
interfere with scripts or other code produced by you (see [Section 5.3](#53-licencing-of-software-and-data)
for more information about licenses).

### 3.1 Source code

Computer code is often a critical part of research and necessary to
validate or reproduce a person's work. This can be model code and code
to post-process data. You should include in your data package any code
along with relevant information about dependencies, the platform it runs
on, required interpreters, compilers, libraries, and the versions used.
Take care to provide a reasonable degree of user documentation for your
software ([Section 4](#4-organizing-and-documenting-data)) and how you have used external software like modeling
code. Source code should always be managed in a version control system,
even if you work by yourself and choose an appropriate open source
software license (cf. [Section 5.3](#53-licencing-of-software-and-data)) from the beginning.

#### 3.1.1 Version control systems

It is good practice to use source code versioning systems such as
[GIT :material-open-in-new:](https://git-scm.com/){:target="_blank"}.
Applications are for instance provided by ETH at
<https://gitlab.ethz.ch/> and WSL provides its own Git repository at
[code.wsl.ch :material-open-in-new:](https://code.wsl.ch){:target="_blank"}.
[EMPA :material-open-in-new:](https://gitlab.empa.ch/){:target="_blank"},
[eawag :material-open-in-new:](https://gitlab.eawag.ch/){:target="_blank"}, and
[MeteoSwiss :material-open-in-new:](https://service.meteoswiss.ch/git){:target="_blank"} also have their own
gitlab instances and [IAC :material-open-in-new:](https://git.iac.ethz.ch/){:target="_blank"} provides an
additional one for its members. Git is a tool for tracking changes in
files in order to record reasons for changes, compare with and
incorporate versions from other people, have multiple people working on
the same code, and maintain several parallel versions of the same code
in a systematic way. Git is designed for collaborative, open source
workflows, [see here](../coding/index.md). However, GIT does not
continuously sync like other tools (polybox, dropbox) but you need to actively synchronize
local and remote versions. GIT is a versioning system for code not data
(do not upload large data volumes). Note that these platforms do not
qualify as "archives" and might disappear tomorrow. Instead, create a
zip- or tar-archive from the version of the source code used in your
work and add it to the data package, while being mindful of third-party
copyright (cf. [Section 3.2](#32-third-party-code)).

#### 3.1.2 Containers for enabling reproducibility

A container is a standard unit of software that packages up code and all
its dependencies so the application runs quickly and reliably from one
computing environment to another. Atmosphere and ocean models are
characterised by complex dependencies, external configurations, and
performance requirements. Containerising such software stacks helps to
provide a consistent environment to ensure security, portability, and
performance. For reproducibility we recommend to build containers with
your software.

Providing the software infrastructure for other researchers to reliably
run your code or containers in the future is out of scope for these
recommendations. For example, CSCS provides state-of-the-art tools for
running container workloads on HPC systems, (e.g.
[podman :material-open-in-new:](https://podman.io/){:target="_blank"}).

### 3.2 Third-party code

Similar to third-party data, copyrighted third-party code should not be
included in the data package. Instead you should refer to exactly the
version used, which is available from a reliable, well-established
repository committed to long-term preservation. For open-source
third-party code, make sure that all dependencies (including versions)
are provided explicitly and containerized with your source code.

### 3.3 Proprietary software

These recommendations might not be fully workable if you use proprietary
third-party software, libraries, languages, or tool-chains. Aim at using
open source software for scientific work, since proprietary tools
diminish the reproducibility and long-term value of your research.

## 4. Organizing and Documenting Data

Throughout your work, keep your research data continuously and
reasonably organised, best from the start. If you come back after three
weeks of holidays and you only need to read your own documentation to
know what is where and what it means, you are OK. If you organise your
data in a directory hierarchy and/or
employ a file naming convention, put some effort into documenting these
structures from the start. Liberally re-factor as your work develops and
these conventions and structures do not match anymore.

### 4.1 Directory Structure

You will need to think about where to save and/or archive (i) the
primary data; (ii) the derived data; (iii) the reports, presentations
and figures. In addition, also consider where to save the tools to do
(iv) the processing and (v) the visualisation. It is highly recommended
to store (i) to (v) in different directories to avoid a chaotic set of
data, programs, and documents in the same directory. They also typically
require different archiving strategies.

Any project consists of different steps: data acquisition; data
processing; visualisation; reporting. Of course, the steps can also run
in parallel. These different steps should also be reflected in a
corresponding directory structure. First of all, it is highly
recommended to create a project directory. This project folder should
contain everything that is specific to this project: data, programs,
figures. Do not put all your programs into one single program folder, if
the programs needed for the project are very specific to this project.
Hence, place them under `project_name/code`. Similarly, data specific
to a project should be placed under `project_name/data`.

Frequently, research data is organised in a hierarchical folder
structure, for example:

```text
project_name/
├── README incl link to git repo for source code and model used (see Sect.4.3.3)
├── Manuscripts/
│   └── Paper1/
│       └── Submission1
└── DATA/
    ├── primary_data/
    │   ├── model-output-year0001.nc
    │   ├── model-output-year0002.nc
    │   └── measurements-year0001.csv
    ├── derived_data_1/
    │   └── tas_CESM2_1850-2010.nc
    ├── derived_data_n/
    ├── third party data/
    ├── published data/
    └── dataset_repository/
```

Note that sometimes it is more appropriate to save the primary data
outside of a project directory in a common shared storage used by many
different projects. This is particularly the case if the primary data is
used in different projects.

A clear hierarchical directory structure is essential to keep track of
different data sets, code versions, and documents. From the beginning,
one should very strictly make sure that different data types are not
stored in the same directories. For instance, programs should be saved
in one place, primary data in another; and also documents and figures
need a separate directory. In this way a data / program chaos can be
avoided.

Often, different versions of processed data are created and saved in
different directories, e.g., because some thresholds in some
postprocessing steps are adapted. It is essential to apply a reasonable
name convention of the folders (see [Section 4.2](#42-file-and-directory-naming)) and to document very clearly in
which way the datasets were created (see [Section 4.3](#43-documentation)), otherwise the danger
exists that many similar datasets exist but it is unclear in which way
they differ and how they could be accurately described in a publication.

### 4.2 File and Directory Naming

#### 4.2.1 General rules

File- and directory-names should adhere to the following conventions to
ensure interoperability across platforms and filesystems and not be a
pain to process programmatically:

- Do not use spaces in filenames! Use an underscore ( \_ ) as a
  substitute.

- Use only alphanumeric characters, minus ( - ), and underscore ( \_ ),
  do not use special characters such as
  `& , * % # ; ( ) ! @ $ ^ ~ ' { } [ ] ? < >`.

- The file extension should be standard and should accurately reflect
  its content

- Dates in filenames (and pretty much everywhere else) should have one
  of the below formats:

  1.  YYYYMMDD

  2.  YYYYMM

  3.  YYYY

> Of course, you can also use hyphens between the individual name parts,
> e.g., YYYY-MM-DD.

- Numbers as part of file names should be left padded with zeros, for
  example: site01_logger001.csv, ..., site12_logger328.csv

- Keep filenames as long as needed but as short as possible

#### 4.2.2 File naming schemes

If a file naming scheme is employed, it should be descriptive and
consistent. Encode attributes of a file as alphanumeric strings
separated by underscores ( \_ ). See for instance the file naming
convention defined for
[CMIP7 :material-open-in-new:](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Global_Attributes/#2-filenames){:target="_blank"}.

If mapping your content to such a convention and directory-structure
becomes too complex, you should consider to employ a proper database. In
particular, if you feel you spend too much effort in your analysis code
to construct the paths for the data files, you are in the process of
implementing a primitive database software by yourself and should step
back and reconsider.

### 4.3 Documentation

#### 4.3.1 Importance

Documentation is essential! You might be able to handle one current
project without documentation. But you will definitely fail if

- you come back to this project half a year later and try to find out
  what your processed data really means, i.e., which version of a
  program was used to create it; or if you have to change something in
  your program and it contains no comments

- you start having to run several projects in parallel (which
  certainly will happen), you often have to switch between different
  projects

- you want someone else to work with your code; nobody wants to apply
  your programs if they are badly structured, not documented. If your
  code is easy to use or adjust, people will more likely be interested
  in using it, and you will also benefit from the spread of your code

#### 4.3.2 Different aspects

There are different aspects of documentation, depending on the kind of
research data:

- primary and derived data: place in the directory of the data a README
  file that describes the data set in sufficient detail (e.g. programs,
  scripts used to create it; parameter settings; etc.). See also [Section
  4.3.3](#433-readme-file) below about the contents of README files.

- programs and scripts: add many comments into your code and markdown
  files to understand later what the different code sections do; just
  reading the comments should give a reasonable outline of your
  algorithm. Optimally, your comments not only describe what is done,
  but also why it is done. Be careful, however, to not clutter your code
  by artificially "over-documenting" obvious statements. Also, keep
  comments in your scripts and programs up-to-date, thus avoiding to
  mislead the reader by wrong comments.

Do not think that there is no need to add comments to your code because
it is only used once for a very specific task and then will never be
used again. Essentially all code can become useful again, if it is well
documented and thus adaptable to new tasks. Documentation comments
should (i) be concise; (ii) represent a reasonable bit of code; and
(iii) be up to date. Keep your comments in line with your changes to
data and/or programs.

Finally, if you find it difficult to comment your code: maybe your
algorithm is too complicated. If your algorithm is not reasonable,
documentation will make life (later) a little easier, but it will not
'rescue' you.

#### 4.3.3 README file

Always place in the directory of the data a README file that describes
the data set in sufficient detail (e.g. programs, scripts used to create
it; parameter settings; from where data was downloaded etc.).

Minimal examples from <https://data.iac.ethz.ch/atmos/> contain:

- Summary

- Contact

- Links

- Last Change

### 4.4 A list of best-practice recommendations

All the data organising aspects discussed are obvious when you read
about them in such a guideline. But during daily work, you will still
find yourself neglecting some of the very basic aspects, be it
because you have to fulfill a nearby deadline, you just want to solve
the problem as quickly as possible, or you simply do not care about who
is coming after you. So think about the following list of best
practices, and try to remember them when you are in a hurry:

- Do not create multiple copies of your data. Use soft or hard links
  instead

- Be sure that important data is always backed up

- Use compression in order to save disk space (see [Data Compression](compression.md))

- Separate programs and scripts from data

- Use a version control system (see [Git best
  practices](../coding/index.md#version-control-with-git))

- Try to split your program in small sub-programs. Re-use functions

- Keep your main results on a reliable storage system

- Add useful comments to your program code. Describe with the comments
  what your code is doing

- From time to time, clean up your directories and remove old and no
  longer used data and files

- Your figures should be easily reproduced at any time by running
  scripts. Avoid "manual" data manipulations

- Try to organise your programs in different directories. Create at
  least one directory per project

- You should always know which is your latest version of your code and
  (processed) data. Old versions should be easy to identify for others,
  or even better, delete old versions not used anymore

- Start documenting your code and your progress from the very beginning,
  and keep your documentation up-to-date.

- Avoid writing huge program code. Try to split your problem into small
  pieces. It will also be easier to re-use smaller program pieces in
  other projects.

- Use variables (or, even better, runtime arguments) instead of hard
  coded paths and system names

- Put variable definitions at the beginning of your code or use
  configuration files which can be easily changed

- Apply data versioning

### 4.5 Some common pitfalls

Some problems can easily be avoided if careful data, program, and
document management is applied. Some common pitfalls are:

- **Different versions of programs and scripts**: Which version was used
  to create a data set? Which version did I use to create a figure? Do I
  keep old versions of scripts? Do I often manually do some steps and
  hence make them difficult to reproduce?

- **Remember where the 'good' data is**! In the course of your work you
  will most likely create several versions of a data set (e.g. a
  blocking climatology): Do you still remember how all the different
  versions were created, in which way they differ? Is it really
  necessary to keep all versions of a data set?

- **Documentation out of date**! In the beginning you might document
  your programs well. Then you change your code, and the documentation
  can be completely outdated or even misleading.

- Strictly separate programs from data; programs ask for a daily backup,
  whereas this is typically not the case for primary and derived data

- Separate programs from reports; programs and scripts are optimally
  handled with a versioning system (Git), whereas this is typically not
  needed for reports and presentations

Avoiding these pitfalls asks for some strategies in organisation. But it
is important to be aware of and actively force yourself to avoid them.
Therefore, do not write your programs in a hurry. Instead, take time to
think about structure and documentation, avoid placing everything in the
same directory because it is convenient at the moment: at a later time
you will be glad if data, documents, and programs are clearly separated
from each other.

## 5. Publishing Data

It is now very common that funding agencies (among them: SNSF, EU) as
well as the institutions from the ETH Domain request the applicants to
write a data management plan (DMP) together with the scientific
proposal, with very detailed information about the research data
workflow (from creation to archiving) and the planned measures to make
this data available to other researchers. Data availability, in this
context, is to be understood in a very broad meaning, comprising not
only the fact that the data should be downloadable, but also the way the
data is organised, formatted and annotated with sufficient and
informative metadata. In the same spirit, many journals request that the
data package is deposited in a data repository with URL(s) properly
referenced in the text.

The underlying goals for such requests stem from the necessity to
properly identify research data in order to be able to share, reproduce
and reuse it.

These data policy regulations have been formalised under the
[FAIR :material-open-in-new:](https://www.go-fair.org/fair-principles/){:target="_blank"}
which are widely recognised. For detailed explanations of these
principles, it is strongly advised to read [SNSF's document on FAIR principles :material-open-in-new:](http://www.snf.ch/SiteCollectionDocuments/FAIR_principles_translation_SNSF_logo.pdf){:target="_blank"}
Generally speaking, it is very valuable to familiarise with the SNSF
policy in terms of [open research data :material-open-in-new:](http://www.snf.ch/en/theSNSF/research-policies/open_research_data/Pages/default.aspx){:target="_blank"}.

### 5.1 Documentation for reproducibility

A publication consists of many parts: primary and derived data,
programs, visualisation scripts, reports and figures. The goal must be
that all results presented in a publication are reproducible with a
reasonable effort. To this aim you should organise your publication data
in a data package. In its simplest form this is a self-contained
directory where all data is saved; at least the data package must
clearly point to all resources needed to reproduce the results.

Depending on the size and complexity of the data package, it might be
useful to describe parts of it in separate README-files, perhaps located
in sub-directories.

The publication proper (article, report) usually contains indispensable
scientific metadata. Please include the [DOI :material-open-in-new:](https://www.doi.org/){:target="_blank"} of
the publication as a resource of the package (see
[example :material-open-in-new:](https://doi.org/10.1177/2053019617740365){:target="_blank"}).

### 5.2 Data Repositories

Data repositories are extremely numerous, with a large diversity in
terms of what they offer as services, how they are indexed on search
engines, whether they provide their service for free or not, etc. In
order to find the best suited data repository, it is very helpful to
search in the
[Registry of Research Data Repositories :material-open-in-new:](https://www.re3data.org/){:target="_blank"}, which nicely
classifies repositories by a large amount of search criteria.

It is important to note that SNSF defines criteria for an acceptable
data repository, i.e., which complies with their open research data
policy:

- it must be non-commercial (as identified in the registry of
  [research data repositories re3data :material-open-in-new:](https://www.re3data.org/){:target="_blank"})

- it must offer globally unique and persistent identifiers (e.g. a DOI)

- it allows to define intrinsic (aka general, basic) and user-defined
  (advanced, specialised) metadata

- it allows to set a license for the data

- metadata are always publicly available, even if the data itself is not

- it ensures interoperability

- it has a long-term preservation plan

Among choices validated by SNSF, we specifically recommend to use the
[ETH Research Collection :material-open-in-new:](http://www.research-collection.ethz.ch/){:target="_blank"}
together with the
[ETH Data Archive :material-open-in-new:](https://www.library.ethz.ch/en/ms/Forschungsdatenmanagement-und-Datenerhalt/ETH-Data-Archive){:target="_blank"},
[EnviDat :material-open-in-new:](https://www.envidat.ch/#/){:target="_blank"} for WSL,
[ERIC :material-open-in-new:](https://opendata.eawag.ch/){:target="_blank"} for eawag or
[Zenodo :material-open-in-new:](https://www.zenodo.org/){:target="_blank"}.
All are safe, support the
[FAIR Principles :material-open-in-new:](https://www.force11.org/group/fairgroup/fairprinciples){:target="_blank"}
and offer excellent visibility of your data on the world wide web. While
the ETH Data Archive has the advantage of being the in-house solution,
at Zenodo, there is a 50 GB per dataset limit, but registered groups may
upload as many datasets as desired, the total repository size being
several petabytes, with constant annual increase. This is not true for
the ETH Research Collection where fees apply above 1 TB of upload per
ETH research group.

Please note that in the very specific context of article self-archiving,
i.e., re-publication of the accepted or published version of an article
text, the ETH Research Collection should be preferred to Zenodo, as
journal self-archiving policies generally distinguish between
'institutional repositories' (like the ETH Research Collection) and
other repository types as

'subject repository' or 'aggregated repository' (Zenodo pertains to the
latter category). Journals are generally more permissive for
self-archiving on an institutional repository than on other repository
types.

### 5.3 Licencing of software and data

#### 5.3.1 General information

Copyright protection for code exists from the time the program code is
created in fixed form (from the moment it is written i.e., coded) and
such protection cannot be waived neither in the EU nor in Switzerland.
Therefore, a person receiving or downloading program code is in
principle not allowed to use such program code without an explicit
permission (the license).

Thus, one of the things that a software developer shall always do is to
apply an appropriate licence to their software when the software is
distributed to someone or placed on an internet page.

According to the copyright, the author of the program code is the
creator of the program code. However, for all program code created
during the official duties of an employment at ETH Zurich, the exclusive
rights of use and the corresponding exploitation rights of such program
code belongs to ETH Zurich, and such program code is considered property
of ETH Zurich.

ETH Zurich has since long implemented a policy for licencing of program
code under an open source license (OSL) and generally supports such
licencing. For the policy please visit the
[Open Source Software page of ETH :material-open-in-new:](https://transfer.ethz.ch/researchers/oss/policies.html){:target="_blank"}
or contact [ETH transfer :material-open-in-new:](https://transfer.ethz.ch/){:target="_blank"}.
Please carefully review such policy and verify if you are allowed to
licence a program code under an open source licence prior following our
recommendations below.

NOTE: Keep in mind that enforcement of a licence is another issue.

#### 5.3.2 Policy at ETH Zurich

ETH supports the use of Open Source licences supported by the
[Open Source Initiative (OSI) :material-open-in-new:](https://opensource.org/licenses){:target="_blank"}.
ETH requires researchers to register all OSS developed at the university
with the
[ETH Data Archive :material-open-in-new:](https://transfer.ethz.ch/researchers/oss.html){:target="_blank"} and release them
using standardized, OSI-approved licenses (MIT, Apache2.0, GNU GPL). All
underlying digital assets, including code and data, must follow the
[FAIR Principles :material-open-in-new:](https://ethz.ch/en/research/open-science/fairdata.html){:target="_blank"} to
ensure they are Findable, Accessible, Interoperable, and Reusable.
Software recorded in the ETH Research Collection with the publication
type "Software" must be registered prior to publication. The
[Business Creation Regulation :material-open-in-new:](https://transfer.ethz.ch/researchers/oss/oss-for-commercialization.html){:target="_blank"}
outlines how research groups can establish ETH spin-offs using OSS
without needing an additional license for the source code. More
information can be found
[under this link :material-open-in-new:](https://unlimited.ethz.ch/plugins/viewsource/viewpagesrc.action?pageId=276476357){:target="_blank"}.

When publishing a paper, which includes, e.g., plotting code in the
supplemental material, this code should be provided with an open source
licence and prior to publication, needs to be registered at the ETH Data
Archive (and subsequently approved by ETH Transfer). A list of projects
registered at the ETH Data Archive can be found at
[this link :material-open-in-new:](https://search.library.ethz.ch/primo-explore/search?query=any,exact,open%20source,AND&tab=default_tab&search_scope=data_archive&sortby=date&vid=DADS&lang=en_US&mode=advanced&offset=0){:target="_blank"}.
Also, when sharing the software on download portals read the
[ETH guidelines :material-open-in-new:](https://ethz.ch/en/industry-and-society/intellectual-property/software/Apps-Download-Portalen.html){:target="_blank"}.

#### 5.3.3 How to add a licence to your datasets

The easiest way of licencing data is done when making the data available
on a data repository (cf. [Section 5.2](#52-data-repositories)): as mentioned above, in order to
fulfill FAIR criteria, the chosen data repository should offer licencing
services. When creating a new entry in your selected repository, the
form will contain a specific menu to define the chosen licence.

#### 5.3.4 Recommended data licences

The above information mainly pertains to licences for software. When it
comes to other forms of data (e.g. tabulated data or databases,
presentations, images, videos, etc.), there are other families of
licences which are more adapted, widely used, and accepted. The most
important and widely used licences are the [Creative Commons (CC) :material-open-in-new:](https://creativecommons.org/){:target="_blank"}.

Creative Commons licencing offers a kind-of **mix** **your licence**
based on your specific needs. It provides a baseline licence and the
possibility to allow or restrict some additional features. For example,
CC-0 can be used to be fully compatible with any Open Research Data
(ORD) regulations but it doesn't require attribution. If a user wishes
to be attributed for their work he/she can use the licence
[CC BY :material-open-in-new:](https://creativecommons.org/licenses/by/4.0/){:target="_blank"}
Now if in addition to attribution the user also wants any potential
derivative work to be licenced under identical or compatible terms
he/she can use the licence
[CC BY-SA :material-open-in-new:](https://creativecommons.org/licenses/by-sa/4.0/){:target="_blank"}
('SA' stands for Share-Alike), however, because it restricts further
usage, users need to be aware that
CC BY-SA
is not considered as a fully open license by opendata.swiss.

A complete list of possibilities that can be combined in a CC licence
can be found at the [creative commons :material-open-in-new:](https://creativecommons.org/licenses/){:target="_blank"} page.
Note, however, that the non-commercial (NC) and the no-derivative (ND)
licence conditions are generally considered non-open licenses. In
particular, we strongly recommend against using the ND licence
condition, as it violates the interoperability as defined by the [FAIR
principle :material-open-in-new:](https://www.go-fair.org/fair-principles/){:target="_blank"}.

Creative Commons licence also offers an
[interface :material-open-in-new:](https://creativecommons.org/choose/){:target="_blank"}
which helps the user to select the correct combination of licence
features. CC-0 and CC-BY are always safe choices as open licenses.

Additional resources:

- [Choosing a licence :material-open-in-new:](https://choosealicense.com/){:target="_blank"}

- [How to licence research data :material-open-in-new:](http://www.dcc.ac.uk/resources/how-guides/license-research-data){:target="_blank"}

- [Why avoid non-commercial licences? :material-open-in-new:](https://freedomdefined.org/Licenses/NC){:target="_blank"}

- [Creative Commons and Open Science :material-open-in-new:](http://doi.org/10.5281/zenodo.840651){:target="_blank"}

#### 5.3.5 Recommended OSLs for software licenses

There are many OSLs out there. It is highly recommended to use one of
the common OSLs since this means that users are familiar with the rights
and obligations coming with such a license.

We recommend to use:

- The [MIT license :material-open-in-new:](https://opensource.org/licenses/MIT){:target="_blank"} if you want a very permissive open source licence

- The [Apache license :material-open-in-new:](https://www.apache.org/licenses/LICENSE-2.0){:target="_blank"} if you want permissive free and open source license

- The [GNU GPL license :material-open-in-new:](https://opensource.org/licenses/gpl-license){:target="_blank"} if
  you want a more restrictive open source licence.

Always keep in mind that **NOT** all OSLs are made the same!

Some of them are more permissive than others (with respect to the
freedom given to the user). Two examples of more permissive licences are
the BSD 2.0 and the MIT licence, respectively. On the other hand, there
are more restrictive open source licences like the
[GNU General Public licence :material-open-in-new:](https://opensource.org/licenses/gpl-license){:target="_blank"}. If
you like how the GPL requires users to share their modifications of your
library, but want to give users more flexibility in licencing their
applications, then the [GNU Lesser General Public
license :material-open-in-new:](https://opensource.org/license/lgpl-3-0){:target="_blank"} might
suit you.

Additional resources:

- A complete list of [open source licences approved by OSI :material-open-in-new:](https://opensource.org/licenses){:target="_blank"}

- Another [licence list :material-open-in-new:](https://opensource.org/licenses/category){:target="_blank"} nicely separated by categories

- Another [very helpful guide :material-open-in-new:](https://choosealicense.com/){:target="_blank"} on choosing your licence

#### 5.3.6 How to add a license to your software

In order to add a licence to your work, two different actions are
required:

1.  to add a proper licence text in your package;

2.  to add a reference to the copyright information and the licence in
    the header of every source file of your package.

For action 1., there is an automatic and a manual way to do it.

If your software is versioned and hosted on a versioning platform like
gitlab, you may use the 'automatic way': on your versioning platform,
where your repository is shown, there is a button to 'Add a license'.
Choose the one you want. This will add the proper text in your
repository, including the modification with your name as author. Make
sure however to review this and replace your name in the copyright
ownership by 'ETH Zurich'. Save the file. This will commit the licence
text into your software package.

If, for some reason, the above 'automatic' method does not apply, you
can add a licence manually: create a file called "Licence.txt" or
"Licence.md" that contains the licence in the top-level directory.

Concerning action 2. (specific header in every source file): the header
should contain two elements:

- the copyright information (`Copyright <YEAR> ETH Zurich`)

- a licence-specific short text. Each licence may specify how this text
  (also called 'licence notice') should be set. One can find this
  information in the corresponding licence notice listed at the
  [Software Package Data Exchange (SPDX) :material-open-in-new:](https://spdx.org/licenses/){:target="_blank"} website.
  Alternatively to this licence short text, it is equivalent to replace
  this by a one-line statement containing the SPDX-standardized
  identifier in the following way:

```text
SPDX-License-Identifier: <standardized SPDX license identifier>
```

For more information on the SPDX specifications, please visit the
[SPDX :material-open-in-new:](https://spdx.org/ids){:target="_blank"} website.

## 6. Archiving Data

The focus of data repositories (cf. [Section 5.2](#52-data-repositories)) lie on publishing and
preserving the accessibility of your data in the long term. Whereas tape
facilities provide a solution for long term storage (LTS) and archiving
of valuable data. Long-term archiving on tapes is recommended for data
that is not meant to either evolve or request frequent read access
anymore. Before you archive, please make sure your data is properly
organised, documented and cleaned up from any unnecessary components
(cf. [Section 4](#4-organizing-and-documenting-data)). The following general recommendations are valid for the
tape archive at ETH and the one at CSCS:

- Add a README.txt file that contains a description, a contact person,
  and if possible an expiration date for your data

- The optimal file size is between 10 and 200 GB

- Files smaller than 10 GB are not suitable for tape archiving

- Files adding to tape archive should be ideally already compressed (see
  [Data Compression](compression.md))

- Group files smaller than 10 GB into .tar.gz or .tar files (in case the
  data is already compressed)

- The larger the tarball, the better is the migrate/recall operation
  performance

- For each file abc.tar or abc.tar.gz, create a file abc.list containing
  the list of files of the tarball. This will allow to inspect the
  contents without actually recalling it from tape

- Archive only those data that you will not need to retrieve soon.
  Recalling data from tape should be an infrequent operation

- IMPORTANT: Once your data has moved to tape, changes are no longer
  possible. The data cannot be changed on tape, but only be deleted or
  retrieved

### 6.1 Tape archiving at ETH Zurich

Each department at ETH has two own data repositories. One accessible
over CIFS (Windows) and one over NFS (Linux). From January 1st 2020 the
Long Term Storage (LTS) service of ETH is free of charge for ETH
members. This might change in the future. Users are not allowed to
directly write data to the tape archive. Each group has a responsible
person for data management. The data manager will review the data before
transferring it to the LTS system. The maximum supported file size is 2
TB. Guidelines to the users and data managers are provided at the
[IAC Wiki :material-open-in-new:](https://wiki.iac.ethz.ch/IT/ETHTapeSystem){:target="_blank"}.

### 6.2 Tape archiving at CSCS

Tape storage at CSCS is offered to projects or organisations that have
been granted a specific quota for that. This is the case for C2SM who
regularly organises data storage for a group of their members at D-USYS.
Please keep in mind that this is not a free service, therefore make an
informed use of it by checking back with your professor/head of group
and/or contacting C2SM about it. More information and technical details
can be found at [CSCS longterm storage :material-open-in-new:](https://docs.cscs.ch/storage/longterm/){:target="_blank"}
or contact [CSCS service desk :material-open-in-new:](https://jira.cscs.ch/plugins/servlet/desk?customize=true){:target="_blank"}.

## Acknowledgements

An earlier version of these guidelines was based on the
[EAWAG data management guide :material-open-in-new:](https://opendata.eawag.ch/docs/research-data-management/archiving-guide.html){:target="_blank"}
published by Harald von Waldow. An earlier version of the section on
software and data licences has been developed by T. Chadha (former C2SM
Scientific Visualization) and counterchecked by ETH Transfer. These
guidelines were written by humans and enhanced using AI.
