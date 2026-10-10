# 9. Future directions and needs

*(target ~600 words; Fig. 6)*

Looking beyond the current gaps, we see five scientific directions that will shape the next generation
of data standards, and three cross-cutting needs that determine whether they succeed (Fig. 6).

**Living data.** Data are increasingly updated and extended throughout their lifecycle, from
acquisition through analysis to publication and reuse, with new annotations, re-processed versions, and
corrected metadata. Standards need to support provenance, modular data that can be
extended without rewriting files, incremental metadata, and integration with analysis tools and
pipelines.

**Data reuse at scale.** Analysis of many datasets at once, including by AI systems, requires data that
can be accessed remotely and in parts, virtual datasets that combine files without copying them, and
better curation and quality control. Ontology annotation becomes essential when no human reads every
dataset [TODO-C29].

**Multimodal data.** As in BBQS, experiments increasingly combine modalities from different communities.
This requires linked data across archives, integration across standards (Section 8), and tools, possibly
AI-assisted, that help map between representations.

**AI and new technologies.** AI-ready data, foundation models trained on neural and behavioral data, and
new recording technologies all create demand for standards for new modalities and for integration with
cloud and high-performance computing. Machine-learning tools may also lower the cost of creating
metadata. However, automation does not remove the need for structure, because a minimal set of required,
validated metadata fields is what makes automatically generated annotation trustworthy and reusable
[TODO-C30].

**Coordination.** Coordination centers such as the BBQS Data Coordination and AI Center have a key role
in connecting projects with standards developers, collecting requirements, and driving the bridges
described above.

Three needs cut across these directions.

- **Education and training**, so that researchers know which standards to use and how, and so that the
  next generation of developers understands the ecosystem rather than a single tool.
- **Outreach and community engagement**, so that requirements from new communities, such as the many
  species and behavior types in BBQS, reach standards developers early.
- **Maintenance and support**, because standards, validators, converters, and archives are research
  infrastructure that must be maintained over decades, while the software around them changes much
  faster. Sustained investment in the people who maintain and integrate these resources, and in the
  integration *between* standards, is a scientific need in its own right [TODO-C31].

Related community efforts, such as the BRAIN Initiative's plans for a knowledge base that connects data
across BRAIN archives, address the archive and knowledge layers of the map and will depend on the
standards discussed here [TODO-C32].

# 10. Conclusion

*(target ~200 words)*

The neuroscience data standards ecosystem is complex, and much of the confusion about what a data
standard is comes from treating its parts as one. Distinguishing six layers, namely archives, dataset
organization standards, file organization standards, ontologies and terminologies, data formats, and
schema languages, each of which solves a different problem, gives researchers and developers a shared
map, shows that FAIR data come from integrating technologies across layers rather than from any single
standard, and makes visible where a project crosses a boundary and should build a bridge instead of
expanding its scope.

Applied to BBQS, the map shows a stack that is complete in the vertical direction, with EMBER, NWB,
BIDS, Psych-DS, HED, and shared terminologies on top of common formats and schema languages, and gives
concrete choices for most neural and behavioral data. It also shows where the ecosystem falls short.
The behavioral constructs that BBQS studies most, such as social interactions and feeding, have no
established representation, and integration between communities is still done project by project.
Closing these gaps requires bridges at every layer, built together by the standards communities and the
programs that depend on them. BBQS, which combines the needs of all these communities in a single
program, is well placed to drive that work.