# RRID lookup checklist (seeds without an RRID)

*Generated 2026-10-09. SciCrunch API search returned 403 for our key (no registry-search permission),
so these are looked up by hand on the public RRID portal (no login needed).*

For each seed: open the search link(s), and if a record clearly describes the same resource, add its
`SCR_xxxxxx` to `seeds.yaml` (`rrid:`); otherwise tick it as **none**. Then run `ecokg rrid-check`.
Generic formats (JSON, YAML, TIFF, …) will often have no RRID; that is fine.

| Done | Seed | Layer | Search | RRID found |
|---|---|---|---|---|
| [ ] | `dabi` | archive | [DABI](https://rrid.site/data/source/nlx_144509-1/search?q=DABI) · [Data Archive for the BRAIN Initiative](https://rrid.site/data/source/nlx_144509-1/search?q=Data%20Archive%20for%20the%20BRAIN%20Initiative) | |
| [ ] | `psych_ds` | dataset_organization | [Psych-DS](https://rrid.site/data/source/nlx_144509-1/search?q=Psych-DS) | |
| [ ] | `dandi_layout` | dataset_organization | [DANDI Layout](https://rrid.site/data/source/nlx_144509-1/search?q=DANDI%20Layout) | |
| [ ] | `sparc_sds` | dataset_organization | [SPARC SDS](https://rrid.site/data/source/nlx_144509-1/search?q=SPARC%20SDS) · [SPARC Dataset Structure](https://rrid.site/data/source/nlx_144509-1/search?q=SPARC%20Dataset%20Structure) | |
| [ ] | `neuroblueprint` | dataset_organization | [NeuroBlueprint](https://rrid.site/data/source/nlx_144509-1/search?q=NeuroBlueprint) | |
| [ ] | `bossdb_dm` | dataset_organization | [BossDB DM](https://rrid.site/data/source/nlx_144509-1/search?q=BossDB%20DM) · [BossDB Data Model](https://rrid.site/data/source/nlx_144509-1/search?q=BossDB%20Data%20Model) | |
| [ ] | `ome_tiff` | data_standard | [OME-TIFF](https://rrid.site/data/source/nlx_144509-1/search?q=OME-TIFF) | |
| [ ] | `ome_zarr` | data_standard | [OME-Zarr](https://rrid.site/data/source/nlx_144509-1/search?q=OME-Zarr) · [OME-Zarr (OME-NGFF)](https://rrid.site/data/source/nlx_144509-1/search?q=OME-Zarr%20%28OME-NGFF%29) | |
| [ ] | `dicom` | data_standard | [DICOM](https://rrid.site/data/source/nlx_144509-1/search?q=DICOM) · [Digital Imaging and Communications in Medicine](https://rrid.site/data/source/nlx_144509-1/search?q=Digital%20Imaging%20and%20Communications%20in%20Medicine) | |
| [ ] | `odml` | data_standard | [odML](https://rrid.site/data/source/nlx_144509-1/search?q=odML) · [Open metadata Markup Language](https://rrid.site/data/source/nlx_144509-1/search?q=Open%20metadata%20Markup%20Language) | |
| [ ] | `edf` | data_standard | [EDF](https://rrid.site/data/source/nlx_144509-1/search?q=EDF) · [European Data Format (EDF/EDF+)](https://rrid.site/data/source/nlx_144509-1/search?q=European%20Data%20Format%20%28EDF/EDF%2B%29) | |
| [ ] | `protein_ontology` | ontology_terminology | [PRO](https://rrid.site/data/source/nlx_144509-1/search?q=PRO) · [Protein Ontology](https://rrid.site/data/source/nlx_144509-1/search?q=Protein%20Ontology) | |
| [ ] | `mrio` | ontology_terminology | [MRIO](https://rrid.site/data/source/nlx_144509-1/search?q=MRIO) · [Magnetic Resonance Imaging Ontology](https://rrid.site/data/source/nlx_144509-1/search?q=Magnetic%20Resonance%20Imaging%20Ontology) | |
| [ ] | `radlex` | ontology_terminology | [RadLex](https://rrid.site/data/source/nlx_144509-1/search?q=RadLex) · [RadLex radiology lexicon](https://rrid.site/data/source/nlx_144509-1/search?q=RadLex%20radiology%20lexicon) | |
| [ ] | `cogpo` | ontology_terminology | [CogPO](https://rrid.site/data/source/nlx_144509-1/search?q=CogPO) · [Cognitive Paradigm Ontology](https://rrid.site/data/source/nlx_144509-1/search?q=Cognitive%20Paradigm%20Ontology) | |
| [ ] | `datacite_schema` | ontology_terminology | [DataCite](https://rrid.site/data/source/nlx_144509-1/search?q=DataCite) · [DataCite Metadata Schema](https://rrid.site/data/source/nlx_144509-1/search?q=DataCite%20Metadata%20Schema) | |
| [ ] | `nbo` | ontology_terminology | [NBO](https://rrid.site/data/source/nlx_144509-1/search?q=NBO) · [Neuro Behavior Ontology](https://rrid.site/data/source/nlx_144509-1/search?q=Neuro%20Behavior%20Ontology) | |
| [ ] | `hcp_atlas` | ontology_terminology | [HCP-MMP](https://rrid.site/data/source/nlx_144509-1/search?q=HCP-MMP) · [HCP Multi-Modal Parcellation](https://rrid.site/data/source/nlx_144509-1/search?q=HCP%20Multi-Modal%20Parcellation) | |
| [ ] | `cde` | ontology_terminology | [CDEs](https://rrid.site/data/source/nlx_144509-1/search?q=CDEs) · [Common Data Elements (NIH/NINDS)](https://rrid.site/data/source/nlx_144509-1/search?q=Common%20Data%20Elements%20%28NIH/NINDS%29) | |
| [ ] | `neurobagel` | ontology_terminology | [Neurobagel](https://rrid.site/data/source/nlx_144509-1/search?q=Neurobagel) | |
| [ ] | `herd` | ontology_terminology | [HERD](https://rrid.site/data/source/nlx_144509-1/search?q=HERD) · [HDMF External Resources Data structure](https://rrid.site/data/source/nlx_144509-1/search?q=HDMF%20External%20Resources%20Data%20structure) | |
| [ ] | `hdf5` | data_format | [HDF5](https://rrid.site/data/source/nlx_144509-1/search?q=HDF5) · [Hierarchical Data Format 5](https://rrid.site/data/source/nlx_144509-1/search?q=Hierarchical%20Data%20Format%205) | |
| [ ] | `zarr` | data_format | [Zarr](https://rrid.site/data/source/nlx_144509-1/search?q=Zarr) | |
| [ ] | `tiff` | data_format | [TIFF](https://rrid.site/data/source/nlx_144509-1/search?q=TIFF) · [Tagged Image File Format](https://rrid.site/data/source/nlx_144509-1/search?q=Tagged%20Image%20File%20Format) | |
| [ ] | `json` | data_format | [JSON](https://rrid.site/data/source/nlx_144509-1/search?q=JSON) · [JavaScript Object Notation](https://rrid.site/data/source/nlx_144509-1/search?q=JavaScript%20Object%20Notation) | |
| [ ] | `tsv_csv` | data_format | [TSV/CSV](https://rrid.site/data/source/nlx_144509-1/search?q=TSV/CSV) · [Delimited text tables (TSV/CSV)](https://rrid.site/data/source/nlx_144509-1/search?q=Delimited%20text%20tables%20%28TSV/CSV%29) | |
| [ ] | `yaml` | data_format | [YAML](https://rrid.site/data/source/nlx_144509-1/search?q=YAML) | |
| [ ] | `mp4` | data_format | [MP4](https://rrid.site/data/source/nlx_144509-1/search?q=MP4) · [MPEG-4 Part 14 video container](https://rrid.site/data/source/nlx_144509-1/search?q=MPEG-4%20Part%2014%20video%20container) | |
| [ ] | `swc` | data_format | [SWC](https://rrid.site/data/source/nlx_144509-1/search?q=SWC) · [SWC neuron morphology format](https://rrid.site/data/source/nlx_144509-1/search?q=SWC%20neuron%20morphology%20format) | |
| [ ] | `precomputed` | data_format | [Precomputed](https://rrid.site/data/source/nlx_144509-1/search?q=Precomputed) · [Neuroglancer Precomputed format](https://rrid.site/data/source/nlx_144509-1/search?q=Neuroglancer%20Precomputed%20format) | |
| [ ] | `fastq` | data_format | [FASTQ](https://rrid.site/data/source/nlx_144509-1/search?q=FASTQ) | |
| [ ] | `bam_cram` | data_format | [BAM/CRAM](https://rrid.site/data/source/nlx_144509-1/search?q=BAM/CRAM) · [BAM/CRAM sequence alignment formats](https://rrid.site/data/source/nlx_144509-1/search?q=BAM/CRAM%20sequence%20alignment%20formats) | |
| [ ] | `loom` | data_format | [Loom](https://rrid.site/data/source/nlx_144509-1/search?q=Loom) | |
| [ ] | `linkml` | schema_language | [LinkML](https://rrid.site/data/source/nlx_144509-1/search?q=LinkML) · [Linked data Modeling Language](https://rrid.site/data/source/nlx_144509-1/search?q=Linked%20data%20Modeling%20Language) | |
| [ ] | `json_schema` | schema_language | [JSON Schema](https://rrid.site/data/source/nlx_144509-1/search?q=JSON%20Schema) | |
| [ ] | `xml_schema` | schema_language | [XSD](https://rrid.site/data/source/nlx_144509-1/search?q=XSD) · [XML Schema](https://rrid.site/data/source/nlx_144509-1/search?q=XML%20Schema) | |
| [ ] | `rdf_owl` | schema_language | [RDFS/OWL](https://rrid.site/data/source/nlx_144509-1/search?q=RDFS/OWL) · [RDF Schema / OWL](https://rrid.site/data/source/nlx_144509-1/search?q=RDF%20Schema%20/%20OWL) | |
