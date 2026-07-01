---
aliases:
  - "Script include Advance structure - Inheritance"
tags:
  - script-include
  - inheritance
  - scripting
  - class-create
---

# Script include Advance structure - Inheritance

Example:
Main Parent script

```jsx
var ParentSCRIPT= Class.create();
ParentSCRIPT.prototype = {

	ParentSCRIPT_LOG_LEVEL: ".bctt.log_level.", // Parameterized for each subclass (each process) - see initialize.
	DEFAULT_PROCESS_TABLE: "",
	DEFAULT_PROCESS_TYPE: "",
	PROCESS_TASK_TABLE: "",
	
	/**
	* Initializes this class with an object parameterized with a 
	* parameter corresponding to either an approval task, process 
	* task or business process
	*
	* @param {GlideRecord} current - the GlideRecord to be assigned 
	* to this class' object global parameter 'current'.
	*/
	initialize: function(currentGr, type, processTable, processType, skipValidation) {
		this.current = currentGr ? currentGr : current;
		this.processTable = processTable ? processTable + "" : this.DEFAULT_PROCESS_TABLE;
		this.processType = processType ? processType + "" : this.DEFAULT_PROCESS_TYPE;
		this.user = ParentSCRIPT.getUser();
		this.debugHelper = new global.BCTT_DebugHelper(this.ParentSCRIPT_LOG_LEVEL+ this.processType.toLowerCase(), type ? type : this.type);
		if(!skipValidation && currentGr){
			this._validateInput();	
		}
	},
	
	getRejectionReasons: function(){
		return new global.BCTT_GlideChoiceListGenerator(this.processTable, "rejection_reason").toArray();
	},
	
	getCancellationReasons: function(){
		return new global.BCTT_GlideChoiceListGenerator(this.processTable, "cancellation_reason").toArray();
	},

	getAskforInfoGroups: function(){
		return new global.BCTT_GlideChoiceListGenerator(this.processTable, "u_ask_info_groups").toArray();
	},
	
	getProcessType: function(){
		return this.processType;
	},
	
	getProcessTable: function(){
		return this.processTable;
	},

	isApprovalTask: function(){
		return this.current.getTableName() == "sysapproval_approver" && this.current.sysapproval.sys_class_name == this.processTable;
	},

	isProcessTask: function(){
		return this.current.sys_class_name == this.PROCESS_TASK_TABLE && this.current.parent.sys_class_name == this.processTable && this.current.parent_type == this.processType;
	},

	isProcess: function(){
		var result = false;
		if(this.processTable == this.DEFAULT_PROCESS_TABLE){
			/* When the process table is the default process table, it means that either the constructor
			was called without arguments or the parent process table was provided. For this scenario, 
			every child table should be considered a process by this definition.*/
			result = this._extendsFromOperations(this.current.sys_class_name);
		} else {
			result = this.current.sys_class_name == this.processTable;
		}
		return result;
	},

	_setCurrent: function(currentGr){
		this.current = currentGr;
	},

	_validateInput: function(){
		if(!(this.isProcessTask() || this.isApprovalTask() || this.isProcess())){
			throw new Error(gs.getMessage("Argument is invalid. The only acceptable objects are {0} processes, approvals or process tasks.", this.processType));
		}
	},
	
	_isMemberOfAssignmentGroup: function(adminOverrides){
		return (gs.getUser().isMemberOf(this.current.getValue("assignment_group")) || this._adminOverrides(adminOverrides));
	},

	_isReturnedBy: function(adminOverrides){
		return (this.current.getValue("returned_by") == this.user.getUserId() || this._adminOverrides(adminOverrides));
	},
	
	_isNotReturnedBy: function(adminOverrides){
		return (this.current.getValue("returned_by") != this.user.getUserId() || this._adminOverrides(adminOverrides));
	},
	
	_adminOverrides: function(adminOverrides){
		return adminOverrides ? gs.getUser().hasRole("admin") : false;
	},
	
	_getExtensions: function(className){
		className = className ? className : this.processTable;
		var result = [];
		var dbObj = new GlideRecord("sys_db_object");
		dbObj.addQuery("super_class.name", className);
		if(className == this.DEFAULT_PROCESS_TABLE){
			dbObj.addQuery("sys_id", "!=", ""); // Remove Process Tasks from the query
		}
		dbObj.query();
		while(dbObj.next()){
			result.push(dbObj.getValue("name"));
		}
		return result;
	},
		
	_extendsFromOperations: function(className) {
		var result = false;
		if(className == this.DEFAULT_PROCESS_TABLE){
			result = true;
		} else {
			var dbObj = new GlideRecord("sys_db_object");
			if (dbObj.get("name", className)) {
				if (!gs.nil(dbObj.super_class)) {
					var parentTable = dbObj.super_class.getRefRecord();
					if(this.DEFAULT_PROCESS_TABLE == parentTable.getValue("name")){
						return true;
					} else {
						return this._extendsFromOperations(parentTable.getValue("name"));
					}
				}
			}
		}
		return false;
	},
	
	type: 'ParentSCRIPT'
};

ParentSCRIPT.getUser = function(userId){
	return new ParentSCRIPT_User(userId);
};

```

Script that Extends the parent:

```jsx
var ChildSCRIPT = Class.create();
ChildSCRIPT.prototype = Object.extendsObject(<application name>.ParentSCRIPT, {
    PROCESS_TYPE: "",
    PROCESS_TABLE: "",
    GROUPS: {
        GROUP: gs.getProperty(".", ""),
        CALL_CENTER: gs.getProperty(".", "") //
    },
    ADMIN_OVERRIDES: (gs.getProperty(".") == "true"),

    initialize: function(current, skipValidation) {
        <application name>.ParentSCRIPT.prototype.initialize.call(this, current, this.type, this.PROCESS_TABLE, this.PROCESS_TYPE, skipValidation);
        this.debugHelper.print("Initialization completed successfully!");
    },
    
    (...) Other methods for ChildScript

```

```jsx
var DebugHelper = Class.create();
DebugHelper.prototype = {
	initialize: function(traceProperty, baseline) {
		this._setBaseline(baseline);
		this.method = ""; // Name of the executing method targeted by the debugger 
		this.gsLog = new global.GSLog(traceProperty);
		this.isInstanceIdOn = false;
		this.debugOn = this.gsLog.atLevel(global.GSLog.DEBUG);
	},

	/**
	* Prints a message using the default log function 'gs.log'.
	* The log is defaulted to the GSLog.DEBUG ('debug') level and is only 
	* printed out if the property passed as input argument to this prototype 
	* constructor is at debug level (see GSLog logging level).
	*
	* @param message {String} the message content to be printed to the system log.
	* @param withoutPrefix {Boolean} indicates whether the message to be printed is
	* to include the default message prefix automaticaly generated by this class or 
	* not, respectively false or true.
	*/
	print: function(message, methodName, withoutPrefix){
		message = (!gs.nil(withoutPrefix) && withoutPrefix == true) ? message : this._getPrintMsgPrefix(methodName) + message;
		this._print(message);
	},

	startMethod: function(methodName){
		this._setMethod(methodName);
		this._print(this._getPrintMsgPrefix() + "started.");
	},

	endMethod: function(methodName, returnValue){
		var returnSuffix = returnValue ? " Returning " + returnValue: "";
		this._print(this._getPrintMsgPrefix(methodName) + "finished." + returnSuffix);
		this._setMethod("");
	},

	includeTimestamp: function(){
		this.gsLog.includeTimestamp();
	},

	includeInstanceId: function(){
		this.isInstanceIdOn = true;
		if(gs.nil(this.instanceId)){
			this._setInstanceId();
		}
	},

	excludeTimestamp: function(){
		this.gsLog._timestampPrefix = false;
	},

	excludeInstanceId: function(){
		this.isInstanceIdOn = false;
	},

	resetInstanceId: function(){
		this.instanceId = "";
	},

	isOn: function(){
		return debugOn;
	},
	
	_setBaseline: function(baseline){
		this.baseline = baseline;
	},

	_setMethod: function(methodName){
		this.method = methodName;
	},

	_setInstanceId: function(){
		this.instanceId = Math.floor(Math.random() * 10000) + 1; // Set the instance ID as a random integer between 1 and 10000
	},

	_print: function(message){
		if (this.debugOn) {
			this.gsLog.logDebug(message);
		}
	},

	_clearPrefix: function(){
		this._setBaseline("");
		this._setMethod("");
	},

	_getPrintMsgPrefix: function(methodName){
		var prefix = "";
		methodName = gs.nil(methodName) ? this.method : methodName;
		
		if(this.baseline)
			prefix += "[" + this.baseline;
		if(methodName)
			prefix += (prefix == "" ? "[" : ".") + methodName;
		if(this.isInstanceIdOn)
			prefix += (prefix == "" ? "[" : "|") + this.instanceId;

		if(prefix != ""){
			prefix += "] ";
		}

		return prefix;
	},
	
	type: 'DebugHelper'
};
```

## Related

- [[Server and Client Side Scripts]]
- [[Scripted Extension Point]]
- [[Impersonate a user via script]]