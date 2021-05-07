from typing import Final

# Annotated Spectrum is a json object that contains information about peptide identified in specific samples.

ANNOTATED_SPECTRUM_PEPTIDE_SEQUENCE: Final = "peptideSequence"
ANNOTATED_SPECTRUM_ORGANISM: Final = "organism"

# Fields for PRIDE PSMs .

ID: Final = "id"
ACCESSION: Final = "accession"
ASSAY: Final = "assayType"
PX_ACCESSION: Final = "pxAccession"
PROJECT_TILE: Final = "title"
FILE_RELATIONS_IN_PROJECT: Final = "submittedFileRelations"
ACCESSION_SUBMISSION_FILE: Final = "accessionSubmissionFile"
ADDITIONAL_ATTRIBUTES: Final = "additionalAttributes"
PROJECT_DESCRIPTION: Final = "description"
SAMPLE: Final = "sample"
SAMPLE_FILE_CHECKSUM: Final = "filechecksum"
PROJECT_SAMPLE_PROTOCOL: Final = "sampleProtocol"
PROJECT_DATA_PROTOCOL: Final = "dataProtocol"
PROJECT_TAGS: Final = "tags"
PROJECT_KEYWORDS: Final = "keywords"
PROJECT_DOI: Final = "projectDoi"
PROJECT_OMICS_LINKS: Final = "project_other_omics"
PROJECT_SUBMISSION_TYPE: Final = "submissionType"
SUBMISSION_DATE: Final = "submissionDate"
PUBLICATION_DATE: Final = "publicationDate"
UPDATED_DATE: Final = "updatedDate"
PROJECT_SUBMITTER: Final = "submitters"
PROJECT_PI_NAMES: Final = "lab_heads"
INSTRUMENTS: Final = "instruments"
SOFTWARES: Final = "softwares"
QUANTIFICATION_METHODS: Final = "quantificationMethods"
COUNTRIES: Final = "countries"
SAMPLE_ATTRIBUTES_NAMES: Final = "sample_attributes"
PROJECT_REFERENCES: Final = "project_references"
PROJECT_IDENTIFIED_PTM: Final = "ptmList"
PRIDE_PROJECTS_COLLECTION_NAME: Final = "pride_projects"
PRIDE_EXPERIMENTAL_DESIGN_COLLECTION_NAME: Final = "pride_experimental_design"
PRIDE_FILE_COLLECTION_NAME: Final = "pride_files"
PRIDE_MSRUN_COLLECTION_NAME: Final = "pride_msruns"
PRIDE_REANALYSIS_COLLECTION_NAME: Final = "pride_reanalysis_collection"
PRIDE_MOLECULES_COLLECTION_NAME: Final = "pride_molecules"
PRIDE_SDRF_COLLECTION_NAME: Final = "pride_sdrf"
PUBLIC_PROJECT: Final = "public_project"
EXPERIMENTAL_FACTORS: Final = "experimentalFactors"
EXTERNAL_PROJECT_ACCESSIONS: Final = "projectAccessions"
EXTERNAL_ANALYSIS_ACCESSIONS: Final = "analysisAccessions"
FILE_CATEGORY: Final = "fileCategory"
FILE_SOURCE_TYPE: Final = "fileSourceType"
FILE_SOURCE_FOLDER: Final = "fileSourceFolder"
FILE_CHECKSUM: Final = "fileChecksum"
CHECKSUM: Final = "checksum"
SUBMITTER_FILE_CHECKSUM: Final = "submitterFileChecksum"
FILE_PUBLIC_LOCATIONS: Final = "filePublicLocations"
FILE_SIZE_MB: Final = "fileSizeMB"
FILE_EXTENSION: Final = "fileExtension"
FILE_NAME: Final = "fileName"
FILE_IS_COMPRESS: Final = "fileCompress"
PRIDE_PEPTIDE_COLLECTION_NAME: Final = "pride_peptide_evidences"
PRIDE_PSM_COLLECTION_NAME: Final = "pride_psm_evidences"
PSM_SPECTRUM_ACCESSIONS: Final = "psmAccessions"
PEPTIDE_SEQUENCE: Final = "peptideSequence"
MODIFIED_PEPTIDE_SEQUENCE: Final = "modifiedPeptideSequence"
REPORTED_PROTEIN_ACCESSION: Final = "reportedProteinAccession"
REPORTED_FILE_ID: Final = "reportedFileID"
EXTERNAL_PROJECT_ACCESSION: Final = "projectAccession"
EXTERNAL_ANALYSIS_ACCESSION: Final = "analysisAccession"
PROTEIN_ASSAY_ACCESSION: Final = "assayAccession"
IDENTIFICATION_DATABASE: Final = "database"
PEPTIDE_UNIQUE: Final = "peptideUnique"
BEST_PSM_SCORE: Final = "bestPSMScore"
RETENTION_TIME: Final = "retentionTime"
CHARGE: Final = "charge"
PRECURSOR_MASS: Final = "precursorMass"
EXPERIMENTAL_MASS_TO_CHARGE: Final = "expMassToCharge"
CALCULATED_MASS_TO_CHARGE: Final = "calculatedMassToCharge"
PRE_AMINO_ACID: Final = "preAminoAcid"
POST_AMINO_ACID: Final = "postAminoAcid"
START_POSITION: Final = "startPosition"
END_POSITION: Final = "endPosition"
SEARCH_ENGINE_SCORES: Final = "searchEngineScores"
MISSED_CLEAVAGES: Final = "missedCleavages"
PRIDE_ANALYSIS_COLLECTION: Final = "pride_analysis_collection"
PRIDE_STATS_COLLECTION: Final = "pride_stats_collection"
STATS_SUBMISSION_COUNTS: Final = "pride_submission_counts"
STATS_ESTIMATION_DATE: Final = "estimationDate"
STATS_COMPLEX_COUNTS: Final = "pride_complex_counts"
MS_RUN_FILE_PROPERTIES: Final = "FileProperties"
MS_RUN_INSTRUMENT_PROPERTIES: Final = "InstrumentProperties"
MS_RUN_MS_DATA: Final = "MsData"
MS_RUN_SCAN_SETTINGS: Final = "ScanSettings"
MS_RUN_ID_SETTINGS: Final = "IdSettings"
MS_RUN_ID_SETTINGS_FIXED_MODIFICATIONS: Final = "FixedModifications"
MS_RUN_ID_SETTINGS_VARIABLE_MODIFICATIONS: Final = "VariableModifications"
MS_RUN_ID_SETTINGS_ENZYMES: Final = "Enzymes"
MS_RUN_ID_SETTINGS_FRAGMENT_TOLERANCE: Final = "FragmentTolerance"
MS_RUN_ID_SETTINGS_PARENT_TOLERANCE: Final = "ParentTolerance"
MONGO_MSRUN_DOCUMENT_ALIAS: Final = "MongoPrideMSRun"
MONGO_FILE_DOCUMENT_ALIAS: Final = "MongoPrideFile"
SAMPLES: Final = "samples"
SAMPLES_MSRUN: Final = "samples_msrun"
PRIDE_ASSAY_COLLECTION_NAME: Final = "pride_assays"
ASSAY_ACCESSION: Final = "assayAccession"
ASSAY_FILE_NAME: Final = "fileName"
ASSAY_TITLE: Final = "assayTitle"
ASSAY_DESCRIPTION: Final = "assayDescription"
ASSAY_DATA_ANALYSIS_SOFTWARE: Final = "dataAnalysisSoftwares"
ASSAY_DATA_ANALYSIS_DATABASE: Final = "dataAnalysisDatabase"
ASSAY_DATA_ANALYSIS_RESULTS: Final = "summaryResults"
ASSAY_DATA_ANALYSIS_PROTOCOL: Final = "dataAnalysisProperties"
ASSAY_DATA_ANALYSIS_PTMS: Final = "ptmsResults"
ASSAY_FILES: Final = "assayFiles"
VALID_ASSAY: Final = "validAssay"
PRIDE_PROTEIN_COLLECTION_NAME: Final = "pride_protein_evidences"
PROTEIN_SEQUENCE: Final = "proteinSequence"
UNIPROT_MAPPED_PROTEIN_ACCESSION: Final = "uniprotMappedProteinAccession"
ENSEMBL_MAPPED_PROTEIN_ACCESSION: Final = "ensemblMappedProteinAccession"
PROTEIN_GROUP_MEMBERS: Final = "proteinGroupMembers"
PROTEIN_DESCRIPTION: Final = "proteinDescription"
PROTEIN_MODIFICATIONS: Final = "ptms"
IS_DECOY: Final = "isDecoy"
BEST_SEARCH_ENGINE: Final = "bestSearchEngineScore"
PROTEIN_REPORTED_ACCESSION: Final = "reportedAccession"
MSRUN_PROPERTIES: Final = "MSRunProperties"
PEPTIDE_ACCESSION: Final = "peptideAccession"
PROTEIN_ACCESSION: Final = "proteinAccession"
PEPTIDE_ACCESSIONS: Final = "peptideAccessions"
PROTEIN_ACCESSIONS: Final = "proteinAccessions"
QUALITY_ESTIMATION_METHOD: Final = "qualityEstimationMethods"
IS_VALIDATED: Final = "isValid"
VALUE: Final = "value"
NUMBER_PEPTIDEEVIDENCES: Final = "numberPeptides"
NUMBER_PSMS: Final = "numberPSMs"
PROTEIN_COVERAGE: Final = "sequenceCoverage"
USI: Final = "usi"
SPECTRA_USI: Final = "spectraUsi"
PSM_SUMMARY_FILE: Final = "fileName"
