---
title: "Text search index debugging script"
aliases:
  - KB0546326
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0546326
kb_number: KB0546326
last_modified: 2024-04-30
---

## Issue

Text search index debugging script 

Using the debugging script

* * *

This script helps to collect information for debugging indexing issue with text search. It is composed of 3 functions. 

1. textSearchHelper(table, documentid, word);  //Checks index matching word and document and return the following information

example of result:

\*\*\* Script: Text index table number: 23 ==> ts\_c\_23\_(1-9)                     //Gives which table index number corresponds to this table  
\*\*\* Script: document: 293bdd4ec0a8016b014651f22fbfdff6 exists in ts\_documents //Confirms the document is indexed in ts\_documents  
\*\*\* Script: word: unauthorized exists in ts\_word                              //Confirms the word is indexed in ts\_word  
\*\*\* Script: wordnumber: 11035                                                 //Number corresponding to the given word in ts\_word  
\*\*\* Script: docnumber: 4358                                                   //Number corresponding to the given document in ts\_document  
\*\*\* Script: TEXT INDEX FOUND: table=ts\_c\_23\_8                                 //Text index table where documentnumber and wordnumber are matched  
\*\*\* Script: Positions: 2Q==                                                   //Positions in the document where the word is found  
\*\*\* Script: Total Weight: 1  
  
2. textSearchWordMatcher(table, word); //Displays all the documents from the specified table which are indexed for this word  
  
3. textSearchDocumentMatcher(table, documentid); //Displays all the words indexed for the document

Script:

//Input variables
var table = "kb\_knowledge";
var documentid = "293bdd4ec0a8016b014651f22fbfdff6";
var word = "unauthorized";

//Checking index matching word and document:
textSearchHelper(table, documentid, word);

//Returning all the documents from the specified table which are indexed for this word:
//textSearchWordMatcher(table, word);

//Returning all the words indexed for the document:
//textSearchDocumentMatcher(table, documentid);

//Confirm if document is in ts\_document, word in ts\_word and if check the index in ts\_c\_... table
function textSearchHelper(table, documentid, word){
var docnumber = 0;
var wordnumber = 0;
var indexnumber = "";

var grindex = new GlideRecord("ts\_index\_name");
if(grindex.get("table",table))
{
	indexnumber = grindex.number;
	gs.print("Text index table number: " + indexnumber + " ==>"+" ts\_c\_"+indexnumber+"\_(1-9)");
}
else
{
	gs.print("Table not found in ts\_index\_name (not indexed)");
	return false;
}

var tsdocument = new GlideRecord("ts\_document");
if (tsdocument.get("document\_id", documentid)) {
    gs.print("document: " + documentid + " exists in ts\_documents");
    docnumber = tsdocument.number;
}
else
{
	gs.print("document does not exist in ts\_document");
	return false;
}

var tsword = new GlideRecord("ts\_word");
if (tsword.get("word", word)) {
    gs.print("word: " + word + " exists in ts\_word");
    wordnumber = tsword.number;
}
else
{
	gs.print("word does not exist in ts\_word");
	return false;
}

gs.print("wordnumber: " + wordnumber);
gs.print("docnumber: " + docnumber);

var indextablename = "";
for (var i = 0; i <= 9; i++) {
    var indextablename = "ts\_c\_" + indexnumber +"\_"\+ i;
    var indexedrecord = new GlideRecord(indextablename);
    indexedrecord.addQuery("word", wordnumber);
    indexedrecord.addQuery("document\_number", docnumber);
    indexedrecord.query();
    if (indexedrecord.next()) {
        gs.print("TEXT INDEX FOUND: table="+indextablename);
        gs.print("Positions: "+indexedrecord.positions);
        gs.print("Total Weight: "+indexedrecord.total\_weight);
        return true;
        }
    }
    
    gs.print("Index NOT found in any of tables "+"ts\_c\_"+indexnumber+"\_(1-9)");
    gs.print("The Word "\+ word + " is NOT linked to the document "\+ documentid + "for " + table + " table");
    gs.print("This word is NOT in this document or indexing is not processed correctly");
    return false;
}

//Returns all the documents from the specified table which are indexed for this word
function textSearchWordMatcher(table, word){
	var wordnumber = 0;
	var indexnumber = "";
	
	var grindex = new GlideRecord("ts\_index\_name");
	if(grindex.get("table",table))
	{
		indexnumber = grindex.number;
		gs.print("Text index table number: " + indexnumber + " ==>"+" ts\_c\_"+indexnumber+"\_(1-9)");
	}
	else
	{
		gs.print("Table not found in ts\_index\_name (not indexed)");
		return false;
	}

	var tsword = new GlideRecord("ts\_word");
	if (tsword.get("word", word)) {
		gs.print("word: " + word + " exists in ts\_word");
		wordnumber = tsword.number;
	}
	else
	{
		gs.print("word does not exist in ts\_word");
		return false;
	}
	
	gs.print("\\n\\nDocuments connected to " + word + " for table: "\+ table);
	var indextablename = "";
	var docnumbers = "";
	for (var i = 0; i <= 9; i++) {
		var indextablename = "ts\_c\_" + indexnumber +"\_"\+ i;
		var indexedrecord = new GlideRecord(indextablename);
		indexedrecord.addQuery("word", wordnumber);
		indexedrecord.query();
		
		while(indexedrecord.next())
		{
			var tsdocument=new GlideRecord("ts\_document");
			tsdocument.get("number",indexedrecord.document\_number);
			gs.print(tsdocument.document\_id + " table: " +tsdocument.table + " Total Weight: " + indexedrecord.total\_weight + " Positions: "+indexedrecord.positions);
		}
	}
}

//Returns all the words indexed for the document
function textSearchDocumentMatcher(table, documentid){
	var docnumber = 0;
	var indexnumber = "";
	
	var grindex = new GlideRecord("ts\_index\_name");	
	if(grindex.get("table",table))
	{
		indexnumber = grindex.number;
		gs.print("Text index table number: " + indexnumber + " ==>"+" ts\_c\_"+indexnumber+"\_(1-9)");
	}
	else
	{
		gs.print("Table not found in ts\_index\_name (not indexed)");
		return false;
	}

	var tsdocument = new GlideRecord("ts\_document");
	if (tsdocument.get("document\_id", documentid)) {
		gs.print("document: " + documentid + " exists in ts\_documents");
		docnumber = tsdocument.number;
	}
	else
	{
		gs.print("document does not exist in ts\_document");
		return false;
	}
	

	var indextablename = "";
	var words = "";
	for (var i = 0; i <= 9; i++) {
		var indextablename = "ts\_c\_" + indexnumber +"\_"\+ i;
		var indexedrecord = new GlideRecord(indextablename);
		indexedrecord.addQuery("document\_number", docnumber);
		indexedrecord.query();
		
		while(indexedrecord.next())
		{
			var tsword=new GlideRecord("ts\_word");
			if(tsword.get("number",indexedrecord.word))
				words += tsword.word + "\\n";
		}
		
	}
	gs.print("words linked to document " + documentid + ":\\n" + words);
}
