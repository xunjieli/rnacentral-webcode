
> **RNAcentral LitScan** is a new text mining pipeline that connects RNA sequences with the latest open access scientific literature. LitScan uses a collection of identifiers (Ids), gene names, and synonyms provided to RNAcentral by the [Expert Databases](/expert-databases) to scan the papers available in [Europe PMC](https://europepmc.org) and keep the publications linked to RNAcentral entries as up-to-date as possible.

LitScan boasts a user-friendly interface, allowing users to easily filter papers based on various facets such as
identifier, article type, the paper section where the ID is located, mentioned organism, journal, and year.

For example, lncRNA `THRIL` is also known as `Linc1992`. Using LitScan, [the corresponding RNAcentral entry](/rna/URS000075D66B/9606?tab=pub)
includes papers about `THRIL`, `Linc1992`, and even `NR_110375` which is another Id for the same gene:

<a href="/rna/URS000075D66B/9606?tab=pub">
    <img class="thumbnail" src="/static/img/litscan-thril.png">
</a>

LitScan is under active development and more sequences will be associated with scientific publications in the future.

<a class="btn btn-primary" href='/search?q=has_lit_scan:"True"'>Browse all sequences with publications</a>

## Use LitScan in your website

The LitScan widget is implemented as an **embeddable component** that can be used by any [Expert Database](/expert-databases) or any
other website. LitScan has already been deployed on the Rfam website (for example, see the [SAM riboswitch](https://rfam.org/family/RF00162#tabview=tab10) page).

Find out more about [how to integrate this widget into your website](https://github.com/RNAcentral/rnacentral-litscan).

## How LitScan works

A list of RNA Ids provided by the Expert Databases is used to
search for open access articles in Europe PMC. The search is performed in two steps:

1. Search [Europe PMC's RESTful WebService](https://europepmc.org/RestfulWebService) for articles that contain an RNA Id anywhere in the text.

    The following query is used:

    <img src="/static/img/query-europe-pmc-v2.png">

    where

    - `"id"` is the Id used in the search
    - `("rna" OR "mrna" OR "ncrna" OR "lncrna" OR "rrna" OR "sncrna")` is used to filter out possible false positives
    - `IN_EPMC:Y` means that the full text of the article is available in Europe PMC
    - `OPEN_ACCESS:Y` it must be an Open Access article to allow access to the full content
    - `NOT SRC:PPR` cannot be a Preprint, as preprints are not peer-reviewed

2. Analyse the full text of the matching articles using [regular expressions](https://en.wikipedia.org/wiki/Regular_expression) to locate the Ids within the
article's title, abstract, or body. From the article that contains the exact Id, LitScan extracts a sentence with the
Id and other relevant information, such as title, authors, journal, etc.

The article will be displayed in the results if the Id is found in **both steps**.

### Example

A [search on EuropePMC](https://europepmc.org/search?query=%22dme-bantam%22%20AND%20%28%22rna%22%20OR%20%22mrna%22%20OR%20%22ncrna%22%20OR%20%22lncrna%22%20OR%20%22rrna%22%20OR%20%22sncrna%22%29%20AND%20IN_EPMC%3AY%20AND%20OPEN_ACCESS%3AY%20AND%20NOT%20SRC%3APPR) for the microRNA precursor [dme-bantam](/rna/URS00002F21DA/7227) ID yielded 13 results as of October 2023.
However, the second step finds the exact string `dme-bantam` **only in 4 articles**, while the other 9 mention
[dme-bantam-3p](/rna/URS00004E9E38/7227) and/or [dme-bantam-5p](/rna/URS000055786A/7227) and appear on the corresponding mature microRNA pages.

<a href="/rna/URS00002F21DA/7227?tab=pub">
  <img class="thumbnail" src="/static/img/litscan-dme-bantam.png">
</a>

## FAQ

### How often are the publications updated?

The publications are updated on an ongoing basis.

### Why is the citation count in LitScan different from Google Scholar, Web of Science or Scopus?

The citation counts per paper shown by the widget may differ from the counts displayed in Google Scholar, Web of Science
or Scopus, as Europe PMC does not have access to the same content as these resources. However, highly cited articles in
Europe PMC correlate with highly cited papers on other platforms. Find out more about the
[Europe PMC citation network](https://europepmc.org/Help#citationsnetwork).

### Why is my article not shown in RNAcentral?

If your article is found in Europe PMC but not in RNAcentral, this could be due to the following reasons:

* **The article was recently published and has not yet been imported into LitScan**

  in this case, it may only be a matter of time before your article is listed in RNAcentral

* **The article does not have any exact Id used in the searches**

  new ids will be scanned on an ongoing basis and the article will be included in the near future

* **Your article is not Open Access in Europe PMC**

  unfortunately there's nothing we can do in this case as we do not have access to the article

### How do you treat identifiers containing special characters?

Note that searching for Ids with special characters may sometimes return articles unrelated to the search terms due to
the use of the [standard Solr tokenizer](https://solr.apache.org/guide/6_6/tokenizers.html#Tokenizers-StandardTokenizer)
in the Europe PMC API that treats whitespaces and special characters as delimiters. This is why the search is performed
in two steps as regular expressions ensure that only articles containing the exact term are used.

### Do you filter out common words?

To prevent false positive matches, we compare RNA Ids against a corpus of common English words to [exclude Ids](https://github.com/RNAcentral/rnacentral-references/blob/main/words_identified_by_corpus.txt)
like `hairpin`, `nail`, `digit`, or `eric` that may correspond to non-RNA entities.

### How are organisms identified? <a style="cursor: pointer" id="organisms" ng-click="scrollTo('organisms')" name="organisms" class="text-muted smaller"><i class="fa fa-link"></i></a>

The organisms listed in the **Mentioned Organisms** facet were extracted from the [ORGANISMS project](https://organisms.jensenlab.org) and may not
be entirely accurate. Find out more about the ORGANISMS project in [this paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0065390).

### How can I find out which Ids are used by LitScan?

The list of Ids can be accessed programmatically. An example Python script to get a list of ids is available below:
