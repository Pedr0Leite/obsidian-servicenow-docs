# ServiceNowOfficialDocs/platform-security/authentication — File Index

Navigation index for AI agents. One row per file in this directory (356 files). Auto-generated from frontmatter — do not hand-edit; regenerate via `scripts/gen_indexes.py` if files are added/removed.

---

| File | Title | Description |
|------|-------|-------------|
| `JWT-Bearer-token-support.md` | Set up OAuth provider with JWT Bearer grant type | JSON Web Tokens (JWTs) enable the capability to configure server-to-server API interactions between ServiceNow and external API providers… |
| `OAuth-token-processor-parm.md` | Change OAuth password parameter | Use this property to ensure only POST body parameters are accepted as input for all supported grant types. |
| `OIDC-SSO-overview.md` | OpenID Connect \(OIDC\) as a Single Sign-On \(SSO\) identity provider \(IdP\) | OpenID Connect (OIDC) is an identity layer built on top of the OAuth protocol, which provides a modern and intuitive Single Sign-on (SSO)… |
| `Scoped-API-generate-JWT.md` | Generate a JSON Web Token \(JWT\) | Create a JSON Web Token (JWT) for representing claims securely between two parties on the ServiceNow AI Platform. |
| `account-recovery-context.md` | Account recovery context | The account recovery context uses a policy to define how and when the account recovery can be established. |
| `acr-properties.md` | Account recovery properties | Use system properties to configure Account Recovery (ACR) on your instance. |
| `activate-approval-esignature.md` | Activate Approval with e-Signature plugin | The Approval with e-Signature plugin (com.glide.e\_signature\_approvals) allows users to approve requests by re-entering their login… |
| `activate-custom-url-plugin.md` | Activate custom URLs | Enable custom URLs to be set up on your ServiceNow instance. You can activate the Custom URL plugin (com.snc.customurl) if you have the… |
| `activate-location-based-access.md` | Activate Location Based Access | Activate the Zero Trust - Location Based Access (com.snc.zero\_trust\_location\_access) to allow admins to configure adaptive… |
| `activate-personal-authentication.md` | Activate Personal Authentication Dashboard | You can activate the Personal Authentication plugin (com.snc.sn\_ihub\_personal\_auth) for Integration Hub if you have the admin role. If… |
| `activate-processor-access-policy.md` | Activate Processor access policy | For Processor, install the Processor Access policy (com.glide.processor.policy) plugin. |
| `activate-rest-api-access-policy.md` | Activate REST API access policy | You can activate the REST API Access Policy plugin (com.glide.rest.policy) if you have the admin role. If the application does NOT include… |
| `activate-rest-api-auth-scope.md` | Activate REST API Auth Scope | You can activate the REST API Auth Scope plugin (com.glide.rest.auth.scope) to link the OAuth entity with authentication scopes. |
| `activate-session-validation-context.md` | Activate session validation context | Use session validation context to restrict access to ServiceNow when hijackers copy a user's session cookies from one device to another to… |
| `activate-soap-api-access-policy.md` | Activate SOAP API access policy | For SOAP API access policy, install the SOAP API Access Policy (com.glide.soap.policy) plugin. |
| `activate-time-limited-authentication.md` | Activate time limited authentication | Time limited authenication activates through the Integration - Multiple Provider Single Sign-On Installer plugin. |
| `activate-trusted-mobile-app.md` | Activate Trusted Mobile app | Activate adaptive authentication with trusted mobile app by using the authentication policy and filter conditions. |
| `active-api-key-hmac.md` | Activate API Key and HMAC Authentication | You can activate the plugin API Key and HMAC Authentication (com.glide.tokenbased\_auth) in your ServiceNow instance. |
| `active-mfa-sms-plugin.md` | Activate the MFA with SMS plugin | For MFA with SMS, install the Multi-factor authentication with SMS (com.snc.authentication.sms\_mfa) plugin. |
| `adaptive-auth-example.md` | Tutorial: Configure adaptive authentication | Use these example steps to configure adaptive authentication on an instance.Learn how to create a criteria record to use as a policy input… |
| `adaptive-auth-filter-criteria.md` | Filter criteria | Filter criteria (also called policy inputs) are used as inputs for policy conditions to verify and meet the requirements of an… |
| `adaptive-authentication-events.md` | Adaptive authentication events | You can use the adaptive authentication events table to know about the events. |
| `adaptive-authentication-plugin.md` | Activate adaptive authentication | You can activate the Adaptive Authentication plugin (com.snc.adaptive\_authentication) for Adaptive Authentication if you have the admin… |
| `adaptive-authentication.md` | Adaptive authentication | Use the Adaptive authentication policy framework to enforce contextual authentication controls to the right users at the right time.… |
| `add-OIDC-entity.md` | Configure an OAuth OIDC provider for accepting third-party token | Configure an OAuth OpenID Connect (OIDC) provider to accept identity tokens generated by a third-party OIDC provider using inbound API… |
| `add-custom-reg-form-field.md` | Add a custom registration form field | You can add custom fields in the user self-registration form. |
| `add-oauth-application-user.md` | Add the OAuth Application User | Add the OAuth Application User field on the OAuth Entity form to use the Client Credentials grant type for OAuth inbound integrations. |
| `add-policy-to-context.md` | Add an authentication policy to an authentication policy context | Add an authentication policy to one of the authentication policy contexts. The authentication context uses the policy inputs and conditions… |
| `add-servicenow-from-the-gallery.md` | Add ServiceNow from the gallery | Add ServiceNow from the gallery to your list of managed SaaS apps on Azure AD. |
| `api-access-policy-prioritization.md` | API access policy prioritization | Learn about the policy prioritization logic if there are multiple API access policy configured for your ServiceNow instance. |
| `api-access-policy.md` | API access policy | API access policy defines the permissions and duration of access to an API. |
| `api-auth-policy-export-processors.md` | Access policy for System or Export Processors | Ability for System or Export Processors to leverage processor access policy to secure all the export endpoints. |
| `api-authentication-policies.md` | API Authentication Policies | Authentication policies evaluate authentication requests based on the specified policy conditions and either allows or denies access… |
| `api-authentication.md` | API Authentication | Authentication configurations for API. |
| `api-inbound-and-outbound.md` | OAuth Inbound and Outbound authentication | OAuth based authentication validates the identity of the client that attempts to establish a trust on the system by using an authentication… |
| `api-key-and-hmac-rest-apis.md` | API Key and HMAC Authentication for inbound REST APIs | Support API tokens for REST API endpoints so that the ServiceNow user name and password isn't visible in the webhook URL. |
| `assign-the-azure-ad-test-user.md` | Assign the Azure AD test user | Assign the Azure AD test user that is created to use Azure single sign-on by granting access to ServiceNow. |
| `auth-policy-contexts.md` | Authentication policy contexts | Use authentication policy contexts to determine how and when your instance enforces authentication policies. |
| `authentication-factors.md` | Authentication factors | Authentication factors help identify and verify callers, allowing only authorized users to access AI voice agents on the ServiceNow AI… |
| `authentication-policies.md` | Authentication policies | Authentication policies evaluate authentication requests based on the specified policy conditions and either allow or deny access depending… |
| `authorization-code-grant.md` | Authorization code grant | The OAuth authorization code grant is a secure and widely used flow for web, mobile, or desktop apps that access user data with user… |
| `authorization-workflow.md` | Authorization code grant workflow | ServiceNow handles both authentication and API access by acting as the authorization and resource server. When single sign-on (SSO) is… |
| `azure-ad-integration-with-saml-2-0.md` | Azure AD Integration with SAML 2.0 | Integrate ServiceNow with Azure Active Directory (Azure AD). |
| `basic-authentication.md` | Basic authentication | Legacy API authentication method using username and password, with restricted usage and varying behaviour in zBoot and upgraded instances. |
| `blacklist-passwords.md` | Exclude passwords through password policies on your instance | Add passwords to the Excluded Password table to prohibit specific passwords from being used by users on your instance. |
| `c_ADFSIntegrationWithSAML2.0.md` | ADFS integration with SAML 2.0 | The ServiceNow Multi-Provider SSO plugin supports a SAML 2. single sign-on (SSO) integration with Microsoft ADFS. |
| `c_AddSupportForDeepLinking.md` | Add deep linking support for SAML | Deep linking allows instances to support direct email links to a particular record in the system. |
| `c_AddingSupportForESignature.md` | Add E-Signature support for SAML | Configure the following properties for E-Signature with Security Assertion Markup Language (SAML) 2.0 update 1. |
| `c_Authentication.md` | Authentication | ServiceNow's authentication validates the identity of a user who accesses an instance, and then authorizes the user to features that match… |
| `c_ChSetRemMeChkbxCookie.md` | Remember me | When the Remember me check box is selected at login, a cookie is stored on the user's computer. This cookie automatically authenticates the… |
| `c_DigestTokenAuthentication.md` | Digest token authentication | The digest token authentication passes user credentials and a digest token within an unencrypted HTTP header. |
| `c_EmailLinksWithSSO.md` | Email links with external authentication | You can use email links when using the digestive token external authentication, however, you must establish how to handle links in email… |
| `c_HighLevelOverview.md` | Nonce process flow | When a customer has implemented the digested token Single Sign-on and wishes to add the security of a nonce, they follow a certain process… |
| `c_IPRangeBasedAuthentication.md` | IP range based authentication | One way to secure a web-based application is to restrict access based on the IP address. |
| `c_IdentityProviderIdPSysProps.md` | Identity Provider \(IdP\) system properties | An IdP generally offers an XML document containing their authentication and logout metadata. |
| `c_Implementation.md` | Implement a nonce | Add a cryptographic nonce to the authentication header to ensure that it can only be used once. |
| `c_ImplementingANonce.md` | Implement a nonce | You can implement a nonce to be used with single sign-on digest authentication. |
| `c_LoginAuthnRequestProcessFlow.md` | Login \(AuthnRequest\) process flow | SAML 2.0 specifies a Web Browser SSO Profile that involves exchanging information among an identity provider (IdP), a service provider… |
| `c_LoginSecurity.md` | Login and authentication security | Configure login security options to control access to your instance. |
| `c_LoginsESSP.md` | Logins and the employee self-service portal | The system keeps track of the first starting page that a user is trying to access even if the user wants to log in to the Employee… |
| `c_LogoutLogoutRequestProcessFlow.md` | Logout \(LogoutRequest\) process flow | During logout, the instance issues the SAML 2.0 LogoutRequest service call to the IdP. |
| `c_MigratingASAML1.1IntegToSAML2.0.md` | Migrating an existing SAML 1.1 integration to SAML 2.0 | To migrate from a SAML 1.1 integration to a SAML 2.0 integration, contact customer support. |
| `c_MultipleProviderSingleSignOn.md` | Multi-Provider single sign-on \(SSO\) | External SSO allows organizations to use several SSO identity providers (IdPs) to manage authentication as well as retain local database… |
| `c_MutualAuthentication.md` | Configure mutual authentication | Mutual authentication establishes trust by exchanging secure sockets layer (SSL) certificates. |
| `c_OAuthApplications.md` | OAuth 2.0 | OAuth 2.0 lets users access instance resources through external clients by obtaining a token rather than by entering login credentials with… |
| `c_OAuthAuthorizationCodeFlow.md` | OAuth authorization code grant flow | Authorization code grant flow allows a user to access a resource by authenticating directly with an OAuth server that trusts the resource,… |
| `c_OAuthClientAPIs.md` | OAuth client APIs | The OAuth client API provides methods to request and revoke OAuth tokens. |
| `c_OAuthImplicitGrants.md` | OAuth implicit grants | ServiceNow instances support the implicit grant of an access token. |
| `c_SAML2.0Troubleshooting.md` | SAML 2.0 troubleshooting | Before contacting support, try the troubleshooting solutions available in the knowledge base on Hi. |
| `c_SAML2.0WebBrowserSSOProfile.md` | SAML | The Security Assertion Markup Language (SAML) is an XML-based standard for exchanging authentication and authorization data between… |
| `c_SAMLConcepts.md` | SAML 2.0 concepts | Familiarize yourself with these SAML concepts. |
| `c_SAMLUserProvisioning.md` | SAML user provisioning | If users exist in your IdP but are not in your instance, SAML user provisioning can automatically create the users in your instance's User… |
| `c_SamJavaDigAlgEncrypt.md` | Sample Java digest algorithm for encryption | This Java algorithm illustrates creating a digest token from an HTTP header. |
| `c_SampleC.md` | Sample C | This C class illustrates creating a digest token from three input parameters. |
| `c_SampleSAML2ResponsesAfterUpdate.md` | Sample SAML 2 responses after the update | The following sections illustrate the new required elements and attributes that the IdP should provide in the SAML Response. |
| `c_SelfServicePasswordReset.md` | Password Reset | The default self-service Password Reset process enables a user to reset the password without assistance from service desk agents. |
| `c_SetTheServiceProviderSPSysProps.md` | Service Provider \(SP\) system properties | These system properties define how the instance interacts with the IdP as a Service Provider. |
| `c_TypicalProcessFlowDiagram.md` | Typical SAML process flow \(diagram\) | A typical SSO logic flow involves looking for an active session, checking user credentials, and creating the necessary token. |
| `c_URLInformationForAnSSOProvider.md` | URL information for an SSO provider | During a login challenge resulting from a URL link into the instance that requires an SSO session, the referring URL might need to be… |
| `c_ValuesInTheUserTableField.md` | Values in the User table field for SAML | Ensure that the integration's User table field contains appropriate matching values. |
| `c_WebServiceSecurity.md` | Web service security | Enforce security using basic authentication, mutual authentication, or WS-Security. |
| `certificate-api-auth.md` | Certificate based authentication | Certificate-based authentication lets you mutually authenticate inbound API requests using certificates from a trusted Certificate… |
| `change-authenticator-app.md` | Change an Authenticator app | Generate a new code to change an Authenticator app on your device. |
| `changes-mfa-enforcement.md` | Changes due to the Multi-factor Authentication enforcement | Information about the changes that are expected due to the MFA enforcement. |
| `client-credential-grant.md` | Client credentials grant | Use the OAuth client credentials grant type for back-end services or automated integrations that access ServiceNow APIs without user… |
| `client-credentials-grant-workflow.md` | Client credentials grant workflow | Authenticate a client application using a client credentials workflow. The client credentials grant workflow is used by back-end services… |
| `client-credentials.md` | Client Credentials | Use the OAuth client credentials grant type for Inbound Integrations from a third party OAuth client to the ServiceNow platform. |
| `client-type.md` | Configure client type for OAuth and SSO records | Configure the Client Type field for OAuth and SSO record related configurations. |
| `config-acr.md` | Configure an account recovery user | Configure an account recovery user to perform account recovery activities on your instance.Configure an account recovery from the Account… |
| `config-private-key-jwt-oidc-sso.md` | Configure Private Key JWT for OIDC based SSO | Configure Private Key JWT for OIDC based SSO integrations. |
| `config-private-key-jwt-outbound-oauth.md` | Configure Private Key JWT for Outbound OAuth | Configure Private Key JWT for outbound OAuth integrations. |
| `configure-a-third-party-id-token.md` | Configure a third party ID token | Configure a third-party ID token to enable secure authentication by verifying user identities through an external IdP. The third-party ID… |
| `configure-adaptive-auth-properties.md` | Configure adaptive authentication properties | After activating adaptive authentication, configure adaptive authentication properties according to your security requirements. |
| `configure-allow-access-policy.md` | Configure an authentication policy | Configure an authentication policy to define inputs and conditions to used to grant access to an instance or enforce multi-factor… |
| `configure-an-oauth-authorization-code-grant.md` | Configure an OAuth authorization code grant | Configure the OAuth authorization code grant to enable secure and interactive user authentication to enable applications to access… |
| `configure-an-oauth-client-credential-grant.md` | Configure an OAuth Client credential grant | Configure the OAuth Client Credentials Grant for secure machine-to-machine authentication without user interaction. It authenticates… |
| `configure-an-oauth-jwt-bearer-grant.md` | Configure an OAuth JSON web token bearer grant | Configuring an OAuth JSON Web Token (JWT) bearer grant secures token-based authentication without user interaction. It enhances security… |
| `configure-an-oauth-resource-owner-password-credential-grant.md` | Configure an OAuth resource owner password credential grant | Configuring an OAuth resource owner password credential (ROPC) grant enables applications to authenticate users by directly using their… |
| `configure-api-key.md` | Configure API key - Token-based authentication | Configure an API key to support authentication for REST API endpoints. |
| `configure-auth-profile-processor.md` | Configure Authentication profile for Processor | Apply authentication profile for the export processors. |
| `configure-azure-ad-sso.md` | Configure Azure AD SSO | Configure Azure AD SSO in the Azure portal. |
| `configure-client-session-access-role.md` | Configure client session access role | The Embedded Session Role Configuration (Client Access Role configuration) record is created by default, which included removal of admin… |
| `configure-custom-url.md` | Set a custom URL as the instance URL | Add a custom URL to your instance configuration to use instead of your ServiceNow URL. |
| `configure-email-otp-service.md` | Configure Email OTP | Configure the Email one-time password (OTP) to enable OTP-based authentication for users in your instance. |
| `configure-facebook-based-sso.md` | Configure a Facebook-based Single Sign-On \(SSO\) | Configure a Facebook-based SSO to your ServiceNow instance. |
| `configure-fido-mfa-factor.md` | Configure FIDO2 as an MFA factor | Configure policy input and condition to display FIDO2 as an MFA factor policy for authentication. |
| `configure-global-blocking-policy-apis.md` | Configure global blocking policy for APIs | Global blocking policy denies the authentication requests of users and APIs based on the specified policy conditions. This policy can be… |
| `configure-hmac.md` | Configure HMAC - Token-based authentication | Configure HMAC to support authentication for REST API endpoints. |
| `configure-kba.md` | Configure knowledge-based authentication | Configure knowledge-based authentication (KBA) to identify and authenticate callers by prompting them to answer preconfigured questions… |
| `configure-mfa-factor-policy-with-email.md` | Configure Email as an MFA factor | Configure policy input and condition to display Email OTP as an MFA factor policy for authentication. |
| `configure-mfa-provider.md` | Configure MFA Provider | Configure SMS and Email with the Provider to ensure every user can login securely. |
| `configure-mfa-with-sso.md` | Configuring MFA with SSO | Enforce MFA with SSO for your users within or outside your organization. |
| `configure-mfa.md` | Configuring Multi-factor Authentication | Configure multi-factor authentication (MFA) to improve your users security posture when using ServiceNow. |
| `configure-okta-verify-push-notification.md` | Configure push notification \(Okta Verify\) | Configure Okta Verify to receive push notifications for secure and convenient identity verification. |
| `configure-personal-authentication.md` | Configure Personal Authentication | You can configure personal OAuth authentication with the REST step in Flow Designer. |
| `configure-recaptcha-sp.md` | Configure Google reCAPTCHA for external user self-registration | To use the Google reCAPTCHA service, you must request an API key pair from Google and then configure the related system properties. |
| `configure-rest-api-auth-scope.md` | Configure REST API Auth scope | Link the OAuth entity with an auth scope to manage the token to access the REST APIs that are linked with the auth scope. |
| `configure-servicenow.md` | Configure ServiceNow | Configure ServiceNow with Azure AD details to use SSO. |
| `configure-sms-as-mfa-factor.md` | Configure SMS as an MFA factor | Configure policy input and condition to display SMS OTP as an MFA factor policy for authentication. |
| `configure-soft-pin.md` | Configure Soft PIN | Users are required to configure Soft PIN before it can be used for authentication with ServiceNow AI Platform. |
| `configure-voice-authentication-factors.md` | Configure voice input for authentication factors | Configure how callers provide authentication responses by speaking or using the phone keypad. |
| `configuring-authentication-factors-for-ai-voice-agents.md` | Configure authentication factors for AI voice agents | To secure voice agent environments, configure authentication factors that first identify the caller, then authenticate them before granting… |
| `connect-3rd-party-oauth-provider.md` | Connect to a third-party OAuth provider | Configure how the client ID and secret are sent to your OAuth provider. |
| `create-OIDC-configuration-SSO.md` | Create an OpenID Connect \(OIDC\) configuration for Single Sign-On \(SSO\) | Create or update an OpenID Connect (OIDC) configuration by using the Multi-Provider SSO plugin. |
| `create-an-authentication-profile.md` | Create an authentication profile | Create an authentication profile and add one or more authentication policies to the profile. You can also configure the ID Token and OAuth… |
| `create-an-azure-ad-test-user.md` | Create an Azure AD test user | Create a test user on Azure AD. |
| `create-an-outbound-rest-message.md` | Create an outbound REST message | Create outbound rest message to authorize instance as authorization server. |
| `create-api-access-policy.md` | Create REST API access policy | Create an API access policy and map an authentication profile to restrict the authentication type for a REST API. For example, you can… |
| `create-api-authentication-policy.md` | Create an API authentication policy | Authentication policies allow you to enforce access restrictions on the APIs based on the specified filter criteria. |
| `create-authentication-profile.md` | Create an authentication profile | Create an authentication profile and add one or more authentication policies to the profile. You can also configure the ID Token and OAuth… |
| `create-cc-sys-prop.md` | Create the Client Credentials system property | Create the glide.oauth.inbound.client.credential.grant\_type.enabled system property to use Client Credentials grant type for OAuth inbound… |
| `create-fips-certificate-for-saml.md` | Create self-signed BCFKS keystore for SAML | Generate a FIPS 140-2 compliant self-signed BCFKS keystore for use in SAML signing and encryption operations within the Multi-Provider SSO… |
| `create-global-api-access-protect-soap.md` | Create a global API access policy to protect SOAP APIs | Create a single global API access policy to protect all the SOAP APIs. |
| `create-group-filter-criteria.md` | Create group filter criteria | Group filter criteria allows or denies user access based on the user group to which the user belongs. |
| `create-ip-filter-criteria.md` | Create IP filter criteria | IP filter criteria allows you to filter users based on the user's IP addresses. You can configure an authentication policy to allow or deny… |
| `create-jwt-endpoint.md` | Create an OAuth JWT API endpoint for external clients \(machine to machine integration\) | OAuth JWT bearer token enables the client web applications to authenticate with your instance seamlessly using the inbound JWT grant type… |
| `create-kba-answer-mappings.md` | Map KBA questions to answers | Create knowledge-based questions and answer mapping to confirm the user's identity. |
| `create-kba-service-mappings.md` | AI voice agent service mapping with KBA | Specify the questions used for caller identification and authentication with a specific AI voice agent service. |
| `create-knowledge-based-answers.md` | Create KBA answers | Create knowledge-based answers for the preconfigured security questions to confirm the user's identity. |
| `create-knowledge-based-questions.md` | Create KBA questions | Create knowledge-based questions to use for caller identification and authentication in AI voice agent interactions. |
| `create-location-filter-criteria.md` | Create Location filter criteria | Use location filter criteria to filter input for users authentication based on the user location. |
| `create-role-filter-criteria.md` | Create role filter criteria | Role filter criteria allows you to filter users based on the roles. You can configure an authentication policy to allow or deny access to a… |
| `create-soap-api-access-policy.md` | Create SOAP API access policy | Create an API access policy and map an authentication profile to restrict the authentication type for a SOAP API. For example, you can… |
| `custom-url-error-fix.md` | Custom URL errors and fixes | A list of common errors and associated fixes for a custom URL setup and configuration.Target Audience: ServiceNow Admin |
| `custom-url-with-multiple-identity-providers.md` | Custom URL with Identity Provider | Set your custom URL with the Identity Provider to enable the user to login with their IdP's. |
| `custom-url.md` | Custom instance URLs | You can enable your ServiceNow instance to be accessible from a company-branded or custom URL. |
| `default-reg-form-fields.md` | Default registration form fields | You can use the default registration form fields or create custom registration form fields. |
| `device-app-registration-details.md` | Registration details of registered devices | View the details of devices that are registered with your ServiceNow instance. |
| `disable-session-limit-user-role.md` | Disable a concurrent session limit by user or role | You can disable a concurrent session limit on a specific user or on a particular role. |
| `e-signature-for-multi-provider-sso.md` | E-signature for Multi-Provider SSO | E-signature with Multi-Provider SSO enables you to use the e-signature properties instead the SAML or OIDC properties for authentication. |
| `email-otp-authentication.md` | Email One-time passwords \(OTP\) authentication | Email OTP for AI voice agents sends a one-time numeric code to the caller's email address. The caller retrieves the code from their email… |
| `enable-password-policies.md` | Enable password policies on your instance | Implement password policy controls at login. Force users to change their password if the password does not meet the password policy… |
| `explore-authentication-factors.md` | Explore authentication factors for AI voice agents | Authentication factors are the elements used for caller identification and authentication. In secure voice agent environments, the process… |
| `explore-digest-token.md` | Explore digest token authentication | The instance reads the HTTP header value and compares its computed hash value of the digest token. |
| `explore-lcs.md` | Explore limit concurrent sessions | You can limit the number of concurrent interactive sessions for a user or role on an instance across all nodes. |
| `explore-mfa.md` | Exploring Multi-factor Authentication | Multi-factor Authentication (MFA) is an authentication method that requires users to provide information other than their basic credentials. |
| `explore-password-requirements.md` | Explore Password complexity requirements | Passwords in your ServiceNow instance must meet complexity requirements. |
| `explore-self-register.md` | Explore Self-register | Use external user self-registration to on-board a large volume of external users to your instance. This feature enhances identity… |
| `explore-tla.md` | Explore Time limited authentication | Support time limited authentication for your ServiceNow instance. |
| `exploring-login-and-authenication-security.md` | Explore login and authentication security | Configure login security options to control access to your instance. |
| `exploring-web-sec.md` | Explore Web service security | Enforce security using basic authentication, mutual authentication, or WS-Security. |
| `external-roles-self-registration.md` | External roles in self-registration | To prevent inadvertently providing access to external users, you can assign the snc\_external role to all external users. |
| `external-user-configuration.md` | Configure a user registration configuration for external users | Create a user registration configuration record to bootstrap the onboarding process of external users to custom ServiceNow applications.… |
| `external-user-registration-plugin.md` | Activate External User Self-Registration | You can activate the External User Self-Registration plugin (com.snc.external\_user\_self\_registration) if you have the admin role. |
| `external-user-self-registration.md` | Self-register to ServiceNow instance | Use external user self-registration to on-board a large volume of external users to your instance. This feature enhances identity… |
| `faq-familiar-with-mfa.md` | MFA metrics | FAQ related to understanding the MFA metrics. |
| `faq-mfa-enforcement-timeline.md` | MFA enforcement timeline | FAQ related to MFA enforcement timelines and why it’s important. |
| `faq-mfa-enforcement.md` | MFA enforcement requirements – What and Why | FAQ related to MFA enforcement and why it’s important. |
| `faq-mfa-exception.md` | MFA enforcement exception | FAQ related to MFA enforcement exception and why it’s important. |
| `faq-mfa-types.md` | MFA types | FAQ related to MFA types and why it’s important. |
| `faq-mfa.md` | Frequently asked questions - Multi-factor Authentication enforcement | Details about some of the FAQs due the MFA enforcement. |
| `faq-reset-mfa.md` | MFA reset | FAQ related to MFA reset and why it’s important. |
| `filter-criteria-apis.md` | Filter criteria for APIs | Filter criteria contains filter conditions or queries that are used as policy inputs for an authentication policy. Policy inputs are used… |
| `generate-idp-metadata-sso.md` | Generate SP metadata for SAML/SSO custom URL installations | A SAML or SSO installation needs the SP metadata generated for the IdP before the custom URL instance generates. |
| `generate-initial-token.md` | Generate Personal Auth Initiator URL | Generate the initial token for a user who doesn’t have access to the credentials page to configure personal authentication. |
| `group-filter.md` | Group Filter | Use group filter criteria to filter users based on the user group to which the user belongs. |
| `identity-provider-attributes.md` | Identity Provider Attributes Filter | Use the Identity Provider attributes that are received from the Security Assertion Markup Language (SAML) response and OpenID Connect… |
| `idp-attributes-oidc.md` | Identity Provider attributes for OpenID Connect | Use the Identity Provider attributes that are received from the OpenID Connect (OIDC) from the Identity Provider (IdP) as a filter criteria… |
| `idp-attributes-saml.md` | Identity Provider attributes for Security Assertion Markup Language | Use the Identity Provider attributes that are received from the Security Assertion Markup Language (SAML) response and OpenID Connect… |
| `idpauthflow.md` | Multi-Provider SSO \(SAML\) IdP authentication flow | Describes the different entities that can authenticate a user through the SAML multi-SSO. |
| `inbound-authentication-profile.md` | REST API access policies | REST API access policies allow you to restrict access to inbound REST APIs based on the authentication type and the specified filter… |
| `ip-filter.md` | IP Filter | Use IP filter criteria to filter the users based on the user's IP addresses. Both IPv4 and IPv6 are supported. |
| `jwt-bearer-grant.md` | JSON Web token bearer grant | Configuring an OAuth JSON Web Token (JWT) bearer grant secures token-based authentication without user interaction. Use this flow when a… |
| `jwt-bearer.md` | JWT Bearer | JSON Web Tokens (JWTs) enable the capability to configure server-to-server API interactions between ServiceNow and external API providers… |
| `jwt-support-for-oauth.md` | Private Key JWT Support for OAuth 2.0 Client Authentication | Support JWT Support for OAuth 2.0 Client Authentication. |
| `knowledge-based-authentication.md` | Knowledge-based authentication \(Security Questions\) | Knowledge-based authentication (KBA) is an identification and authentication method that verifies callers by prompting them to answer… |
| `lf-for-session-access.md` | Use Location Filter for Session Access | Use the location filter criteria created in Session Access to reduce roles based on the location of the user. |
| `limit-concurrent-sessions-plugin.md` | Activate and configure limit concurrent sessions plugin | You can activate the Limit Concurrent Sessions plugin (com.glide.limit.concurrent.sessions) if you have the admin role. |
| `limit-concurrent-sessions.md` | Limit concurrent sessions | You can limit the number of concurrent interactive sessions for a user or role on an instance across all nodes. |
| `local-authentication.md` | Local authentication | Use ServiceNow local authentication to secure the users login on a local device. |
| `location-filter.md` | Location Filter | Location filter criteria can be used as filter input for users based on the user location. |
| `log-in-multi-provider-sso.md` | Log in using Multi-Provider SSO | The recommended and most efficient method for users to log in using Multi-Provider SSO is to use a specifically configured URL. |
| `login-metrics.md` | Log in Metrics | Log in Metrics displays the log in trends on the ServiceNow. |
| `manage-your-trusted-device.md` | Manage your trusted device | Manage your trusted device from the Trusted Device registration page. |
| `mfa-auth-app.md` | Authenticator Applications | Use third party authenticator applications to generate temporary MFA pass codes. |
| `mfa-auth-config.md` | Authenticator configuration options | Use the Authenticator Configuration page to manage authenticator options on your instance. |
| `mfa-auth-context.md` | Multi-factor Authentication context | The Multi-factor Authentication (MFA) policy context uses a policy to define how and when MFA is enforced during the login process. |
| `mfa-dashboard.md` | MFA Dashboard | View the different MFA metrics to understand the MFA adoption and usage. |
| `mfa-enforcement-properties.md` | MFA enforcement properties | Configure the properties for MFA enforcement from Yokohama and upgrade to Yokohama. |
| `mfa-enforcement-scope.md` | MFA enforcement scope | FAQ related to MFA enforcement scope and why it’s important. |
| `mfa-enforcement.md` | Multi-factor Authentication enforcement | Enforcement of MFA for non-SSO logins to ServiceNow from the Yokohama release. |
| `mfa-factor-policies.md` | Multi-Factor Authentication factor policies | Use the MFA factor policies to specify the types of authentication factors that you would like to permit for your instance. |
| `mfa-guided-setup.md` | MFA Guided Setup | Use the MFA Guided Setup to step through the initial configuration of the MFA module and understand the requirements for MFA enforcements. |
| `mfa-landing.md` | Multi-factor authentication | Learn how to activate, use, and configure Multi-factor authentication (MFA). |
| `mfa-methods.md` | Multi-factor Authentication verification methods | ServiceNow's MFA supports verification methods such as Authenticator App, Fast IDentity Online 2 (FIDO2) and Time-based One-Time Password… |
| `mfa-metrics.md` | MFA Metrics | View the different MFA metrics to understand the MFA adoption and usage. |
| `mfa-policy-criteria.md` | Configure adaptive authentication policy-based multi-factor criteria | Use adaptive policies to determine which users must use two-step multi-factor (MFA) verification. |
| `mfa-properties.md` | Multi-factor Authentication system properties | Use system properties to enable and customize MFA to meet your security requirements. |
| `mfa-role-criteria.md` | Configure role-based multi-factor criteria | Use role based multi-factor criteria to enforce Multi-factor authentication for all users assigned to specific roles. |
| `mfa-setup-bio-auth.md` | Register a biometric authenticator | Register a biometric authenticator to use as part of your MFA login. |
| `mfa-setup-hardware-key-auth.md` | Register a hardware security key | Register a hardware key to use as part of your MFA login. |
| `mfa-setup-profile.md` | Set up Multi-factor authentication on your user profile | Enable multi-factor authentication for your account in your user profile settings. |
| `mfa-sso.md` | Multi-factor Authentication with Single Sign-On | You can use MFA with an SSO provider for your ServiceNow instance. |
| `mfa-use.md` | Using Multi-factor authentication | Learn how to use multi-factor authentication tools to securely access your instance. |
| `mfa-web-auth.md` | Web Authentication | Your users can use hardware keys or their device's biometric readers (FIDO2) to authenticate to an instance. |
| `mfa-with-email.md` | Email as an MFA factor | Multi-factor authentication (MFA) with Email as a factor for your authentication. |
| `mfa-with-fido.md` | FIDO2 as an MFA factor | You can configure FIDO2 as an MFA factor policy to enforce MFA for yours. |
| `mfa-with-sms.md` | SMS as an MFA factor | Multi-factor authentication (MFA) with SMS as a factor for your authentication. |
| `mobile-adaptive-authentication.md` | Adaptive authentication for Trusted Mobile apps | Access your ServiceNow from untrusted networks by using the Now Mobile app. |
| `multi-factor-authentication-criteria.md` | Multi-factor Authentication criteria | Use MFA criteria to determine which users and roles must use two-step verification. |
| `multi-factor-authentication-providers.md` | Multi-factor authentication Providers | Use MFA providers to configure SMS and Email based authentication to ensure every user can login securely. |
| `new-inbound-integrations.md` | New Inbound integrations experience | The new inbound integration workflow in the ServiceNow Machine Identity Console provides enhanced experience for managing inbound… |
| `oauth-auth-code-flow-state-parm.md` | Authorization code flow state parameter requirement | The glide.oauth.state.paramater.required system property enables the State parameter to be required in an OAuth request for authorization… |
| `oauth-inbound-and-outbound.md` | OAuth | OAuth based authentication validates the identity of the client that attempts to establish a trust on the system by using an authentication… |
| `oauth-inbound.md` | OAuth Inbound | OAuth Inbound authentication allows trusted external applications to securely access ServiceNow APIs, ensuring controlled and authorized… |
| `oauth-outbound.md` | OAuth Outbound | OAuth outbound enables you to pull data from a third-party provider to your instance. |
| `old-inbound-integrations.md` | Old Inbound integrations experience | Old experience - Inbound integrations. |
| `password-complexity-requirements.md` | Password complexity requirements | Passwords in your ServiceNow instance must meet complexity requirements. |
| `password-policy-properties.md` | Password policy properties | The password policy properties enable you to administrate password policies, exclude list passwords, and apply a password policy during… |
| `personal-authentication.md` | Personal Authentication | Personal authentication enables you to securely connect and manage your OAuth-based integrations like Microsoft OneDrive or Google Drive. |
| `personal-oauth-token.md` | Get Personal OAuth Token \(using GlideOAuthClient\) | Check whether the user has a personal OAuth token. Use it to confirm valid access before running REST steps or integrations that require… |
| `post-auth-context.md` | Post-authentication context | The Post Authentication policy context defines how and when a policy is enforced during the login process. The policy used in this context… |
| `pre-auth-context.md` | Pre authentication context | The pre authentication policy context defines how and when a policy is enforced during the login process. The policy used in this context… |
| `push-notification-okta-verify.md` | Push notification - Okta Verify | The Okta Verify app push notification enables users to securely approve authentication requests directly on their enrolled mobile devices. |
| `r_CommonConnectionErrors.md` | Common IdP connection errors | The following table describes some of the common IdP connection errors and their solutions. |
| `r_EventQueueLoginActivities.md` | Monitor the event queue for login activities | Every single sign-on integration creates events for login activities. |
| `r_EventQueueLoginEvents.md` | Event queue login events | The SAML 2.0 integration creates events for login activities. |
| `r_ForcingLoginViaSSOOnly.md` | Redirect single sign-on \(SSO\) logins | When SSO is enabled, you can redirect users to specific pages or direct users to login locally. |
| `r_InstallationExits.md` | Installation exits | Installation exits are customizations that exit from Java to call a script before returning back to Java. |
| `r_InstalledWithMultiProviderSSO.md` | Multi-Provider SSO properties, tables, and scripts | The Integration - Multiple Provider Single Sign-On Installer plugin includes the following system properties, tables, and scripts. |
| `r_OAuthAPIRequestParameters.md` | OAuth API request parameters | Learn about the OAuth API request parameters that access token requests use. |
| `r_OAuthAPIResponseParameters.md` | OAuth API response parameters | The OAuth 2.0 API produces a JSON response containing the following parameters as name:value pairs. |
| `r_OAuthProfileParameters.md` | OAuth parameters for default profile support | The default profile feature requires a set of parameters that you can use with the setParameter() API to specify the OAuth requestor, a… |
| `r_SampleImplements.md` | Sample digest token implementations | Here are several samples of creating a digest token. |
| `r_SetAdvancedSystemProperties.md` | \(Optional\) Advanced SAML properties | The following advanced settings allow you to further increase security and debug the integration. |
| `reference-topic-multi-factor-authentication.md` | Reference topic - Multi-factor Authentication | Reference topic related to the configuration of MFA. |
| `register-trusted-device.md` | Register a trusted device | Register a trusted device to access the ServiceNow instance outside the network. |
| `reset-multi-factor-authentication.md` | Reset Multi-factor Authentication \(MFA\) for users | Administrators can reset MFA for users who deleted the app, lost access to the device, or have no alternative MFA associated with their… |
| `reset-your-password.md` | Configure password for a user | Set your user's password for the instance based on the password policy that is configured. |
| `resource-owner-password-credential-workflow.md` | Resource owner password credential grant workflow | This flow is used in legacy or highly controlled environments where secure alternatives aren't feasible. The client app directly collects… |
| `resource-owner-password-grant.md` | Resource owner password credential grant | Configuring an OAuth Resource Owner Password Credential (ROPC) grant enables applications to authenticate users by directly using their… |
| `rest-api-auth-scope.md` | REST API Auth Scope | Use the REST API Auth Scope to provide access to a specific REST API |
| `rest-api-auth_scope-properties.md` | REST API Auth Scope properties and tables | The REST API Auth Scope plugin (com.glide.rest.auth.scope) includes the following system properties, tables, and scripts. |
| `rest-api-scope-troubleshooting.md` | REST API scope troubleshooting | Troubleshooting actions can help resolve common issues when setting up or running the REST API scope. |
| `role-filter.md` | Role Filter | Use role filter criteria to filter users based on their roles. |
| `saml-errors.md` | Multi-SSO \(SAML 2.0\) errors and fixes | A list of common errors and associated fixes for a Multi-SSO (SAML 2.0) setup and configuration. |
| `saml-guided-tour.md` | SAML Guided Tour | Use the SAML Guided Tour to configure SAML for single sign-on. |
| `session-context.md` | Session validation context | Use the Session Validation Context as an additional layer of protection against session or cookie hijacking. |
| `set-session-limit-user-role.md` | Set a concurrent session limit by user or role | You can set a concurrent session limit on a specific user or on a particular role. |
| `set-your-password-policy.md` | Configure your password policy | Password policy criteria enables you to secure your password and adhere to the minimum password complexity requirements. |
| `sms-otp-authentication.md` | SMS One-time passcode \(OTP\) authentication | SMS one-time password (OTP) authentication is a method used to verify user identity by sending a temporary, numeric code to the user's… |
| `soap-api-access-policies.md` | SOAP API access policies | SOAP API access policies allow you to restrict access to inbound SOAP APIs based on the authentication type and the specified filter… |
| `softpin-authentication.md` | Soft PIN authentication | Soft PIN is a six-digit numeric PIN that verifies a caller's identity during an AI voice agent session. |
| `sp-ext-user-self-reg.md` | Enable external user self-registration for Service Portal | Enable external users to register to a ServiceNow app through Service Portal. |
| `sso-acct-recovery.md` | Account recovery \(ACR\) | Administrators can configure account recovery (ACR) to perform recovery activities such as addressing SSO misconfiguration or expired… |
| `sso-configurations.md` | Multi-Provider SSO configurations | You must perform several steps to set up Multi-Provider SSO, including configuring properties, creating identity providers (IdPs), and… |
| `sso-esignature-approval-SAML.md` | Use Multi-Provider SSO to set up an SSO approval for a SAML 2.0 authentication | An SSO approval with e-signature requires configuration on the SAML IdP and the ServiceNow instance. |
| `sso-esignature-approval-oidc.md` | Use Multi-Provider SSO to set up an SSO approval for an OIDC authentication | An SSO approval with e-signature requires configuration on the SAML IdP and the ServiceNow instance. |
| `t_AccessControl.md` | IP Address Access Control | Apply an IP access control to outbound traffic, inbound traffic, or bidirectional traffic. The system only blocks an IP address if a… |
| `t_ActivateMultipleProviderSSO.md` | Activate Multi-Provider SSO plugin | This integration requires the Integration - Multiple Provider Single Sign-On Installer (com.snc.integration.sso.multi.installer) plugin. |
| `t_ActivateOAuth.md` | Activate OAuth | By default, the OAuth 2.0 (com.snc.platform.security.oauth) plugin is active on new and upgraded instances. If the plugin is not active on… |
| `t_AddSupportForIntegrations.md` | Integrating SAML 2.0 with other features | You can integration your SAML 2.0 solution with other features like E-Signature, deep linking, and ADFS. |
| `t_AdministerSAMLUserProvisioning.md` | Administer SAML user provisioning | Update the User table with the users in your IdP by first setting up field mapping and then enabling user provisioning through Multi-SSO… |
| `t_AllowUsersToChooseTheLoginIdP.md` | Enable users to choose the identity provider for login | SSO federation support enables users to choose which IdP to log in to. |
| `t_AuthorizeAccessEndpiont.md` | Authorize access to an OAuth endpoint using auth code flow | End users who own a protected resource on the ServiceNow instance must authorize access to the resource before the instance can provide the… |
| `t_CloneAnInstanceWASAMLIntegration.md` | Clone an instance with a SAML integration | Clone an instance with a SAML integration. Before you clone an instance that uses SAML 2.0, preserve the SAML SSO-related settings on the… |
| `t_ConfigureADFSClaimRules.md` | Configure the ADFS relying party claim rules | Edit the claim rules to enable proper communication with the instance. |
| `t_ConfigureADFSRelyingParty.md` | Configure an ADFS relying party | Take the instance metadata and import it into your ADFS server. However, manual configuration of the relying party appears to be easier to… |
| `t_ConfigureMultiProviderSSOProps.md` | Configure Multi-Provider SSO properties | Configure SSO properties and also add a property to the System Properties table to configure an IdP inclusion list. |
| `t_ConfigureUsersMultiProviderSSO.md` | Configure users for Multi-Provider SSO | Administrators can configure Multi-Provider SSO for individual users or for all users who belong to a company. You cannot configure… |
| `t_CreateASAML2Upd1SSOConfigMultiSSO.md` | SAML 2.0 configuration using Multi-Provider SSO | You can create or update a SAML 2.0 SSO configuration from the Multi-Provider SSO feature. |
| `t_CreateASAMLLogoutEndpoint.md` | Create a SAML logout endpoint | Create a SAML logout endpoint to allow single logout. |
| `t_CreateEndpointforExternalClients.md` | Create an endpoint for clients to access the instance | Create an OAuth application endpoint for external client applications to access the ServiceNow instance. |
| `t_CreateUpdateIdentityProvider.md` | Create an external identity provider | After you have configured the multi-provider SSO properties, you can update or create new SAML 2.0 or digest token identity provider. |
| `t_CreatingAServiceProviderKeyStore.md` | Create a service provider key store for SAML | Create a Java key store containing the following items for your instance to sign logout requests. |
| `t_DefineADFSServiceURL.md` | Set up ADFS for SAML | Set up ADFS for SAML. This procedure uses ADFS 2.0 and shows samportal.example.com as the ADFS website. Replace this with your ADFS website… |
| `t_EnableSignedLogoutRequests.md` | \(Optional\) Enable signed logout requests | Some IdPs require the Service Provider to sign logout requests with a certificate. |
| `t_EnableSvcProviderInitiatedAuth.md` | \(Workaround\) Enable service provider-initiated authentication | Use this workaround if authentication fails because you do not have SAML 2.0 Update 1. This issue can happen if users attempt to skip IdP… |
| `t_EnableTheLogoutConfirmPrompt.md` | Configure the logout confirmation prompt | You can enable a logout confirmation prompt to prevent users from inadvertently logging themselves out. |
| `t_EnterDigestPropsMultiProviderSSO.md` | Configure the digest properties for multi-provider single sign-on \(SSO\) | After enabling a digest installation exist script, configure properties for multi-provider SSO. |
| `t_FindDeniedIPAddresses.md` | Find denied IP addresses | Find Denied IP addresses in the instance's node log files. |
| `t_GenerateServiceNowSPMetadata.md` | Generate instance service provider \(SP\) metadata for SAML | As part of your SSO configuration, you can generate the instance SP metadata to provide to the IdP. |
| `t_InstallASPKeystoreSigningSAMLReqs.md` | Install a service provider keystore for signing SAML requests | Use the following steps to remove the existing example key store and install your own Service Provider key store containing your public and… |
| `t_InstallTheIdentityProviderCert.md` | Install the identity provider certificate | You can paste a PEM certificate into a X.509 Certificate form so the identify provider can verify communications with the service provider. |
| `t_InstanceAsAuthorizationServer.md` | Authorization code flow example: ServiceNow instance as authorization server | You can use an instance as an authorization server to issue tokens to a client using authorization code flow. |
| `t_LockoutForFailedLogins.md` | Specify lockout for failed login attempts | The system provides inactive script actions that enable you to specify the number of failed login attempts before a user account is locked… |
| `t_LogOnWithMultifactorAuth.md` | Log in with Multi-factor Authentication | Login with MFA when it is enabled by your administrator on your instance. |
| `t_LoginScenarios.md` | Define login scenarios | You can direct all users to the same page after login. |
| `t_MakeAPagePublic.md` | Make UI pages public or private | You can make pages public if you want your users to see the pages without logging in. |
| `t_ManageTokens.md` | Manage OAuth tokens | Open OAuth tokens to provide access to restricted resources. |
| `t_MatchUserTableFieldToNameIDToken.md` | Determine what User table field matches the NameID token | Identity providers specify what format the NameID token has. |
| `t_ModifyPasswordResetNotification.md` | Modify the Password Reset notification email text | Users of the self-service Password Reset process receive an email notification when they request password reset. You can modify the text of… |
| `t_OptEnableProvidingAuthContxtClass.md` | \(Optional\) Enable providing an authentication context class for SAML | You can enable the instance to send an authentication context class request to the IdP containing your instance's preferred authentication… |
| `t_OptSetKeystorePropsSignLogoutReqs.md` | \(Optional\) Set keystore properties for signing logout requests for SAML | Set the keystore properties to enable the integration to sign logout requests by using your signed server and signed CA certificates. |
| `t_ReplacingAMissingCertificate.md` | Replace a missing certificate for SAML | If the Certificate module displays a blank page, the SAML 2.0 certificate record has been deleted. You can replace the missing certificate… |
| `t_RequireMultifactorAuthForAUser.md` | Configure user-based multi-factor criteria | Use user based multi-factor criteria to enable MFA for a user. |
| `t_RevokeOAuthToken.md` | Revoke an OAuth token | You might want to revoke an OAuth access or refresh token for security reasons. |
| `t_SetPwdResetProps.md` | Configure Password Reset properties | You can specify properties that configure the Password Reset experience for end users. |
| `t_SetTheAudienceURL.md` | Set the audience URL for SAML | Enable your instance to verify that it is the intended recipient of a SAML response by using the Audience property. |
| `t_SetTheAuthnRequestServiceURL.md` | Set the AuthnRequest service URL | Using the IdP's metadata, set the request service URLs for the integration's IdP. |
| `t_SetTheIdPIssuerURL.md` | Set the IdP issuer URL | Provide the URL to the IdPs who will issue the security token. |
| `t_SetTheIdPNameIDPolicy.md` | Set the IdP NameID policy | Specify what format the IdP uses for the NameID token. |
| `t_SetTheInstanceURL.md` | Set the instance URL for SAML | Set the instance-specific URLs so that the IdP can authenticate users. |
| `t_SetTheOAuthProperty.md` | Set the OAuth property | To generate OAuth 2.0 tokens to registered applications, the com.snc.platform.security.oauth.is.active property must be active for the… |
| `t_SetTheSingleLogoutRequestSvcURL.md` | Set the SingleLogoutRequest service URL | Set the request service URLs for the integration's IdP by using the IdP's metadata. |
| `t_SetUpMultiFactorAuthUponLogin.md` | Set up Multi-factor authentication for the first time | If your administrator enabled MFA on your profile but you have not yet set up the application, you can set it up upon login. |
| `t_SetUpNameIDPolicy.md` | Set up a NameID policy for SAML | Set up a NameID policy for SAML. SAML 2.0 requires the IdP to exchange a NameID token with the service provider. |
| `t_SetUpServiceNowForADFS.md` | Set up the instance for ADFS | Configure your instance and SAML 2.0 settings to work with ADFS. |
| `t_SettingUpOAuth.md` | Set up OAuth | Set up and activate OAuth, enable the OAuth system property, create an OAuth application endpoint for external client applications to… |
| `t_SpecifyingALoginLandingPage.md` | Specify a login landing page | By default, users see their homepage upon login. You can specify a different login landing page by using a system property or the content… |
| `t_SupportKerberosAuthentication.md` | \(Workaround\) Support Kerberos authentication | A workaround is available for the SAML 2.0 integration that changes the authentication context from forms-based authentication to… |
| `t_TestIdPConnections.md` | Test IdP connections | Testing the connection to an IdP validates the settings before enabling external authentication. |
| `t_TestTheADFSConfiguration.md` | Test the ADFS configuration | Test your ADFS configuration to verify that it is properly functioning as an identity provider. |
| `t_TestTheIntegration.md` | Test the SAML integration | Test the SAML integration after you complete all the other setup tasks. |
| `t_TroubleshootScriptIssuesWithSAML.md` | Troubleshoot script issues with SAML | Troubleshoot script issues with SAML. You might encounter script issues if SAML is already active at the time that you activate Multiple… |
| `t_UpdateExistingSAML2.0Integration.md` | Update your existing SAML 2.0 integration | Update your existing SAML 2.0 integration. |
| `t_UsingESSPagesWithMultiProviderSSO.md` | Use Service Portal with Multi-Provider SSO to redirect a URL | Service Portal uses a combination of system properties and script includes to determine how the system handles URL redirects for users… |
| `third-party-id-token.md` | Third party token grant | The third party token grant enables ServiceNow to accept identity tokens from trusted external identity providers, such as Azure AD or… |
| `third-party-token-worflow-for-user-accounts.md` | Third party token workflow for user accounts | This workflow can be used to integrate third-party identity providers (IdPs) with ServiceNow for secure API access. It allows client… |
| `third-party-token-workflow-for-service-accounts.md` | Third party token workflow for service accounts | Create a service account in ServiceNow to represent the identity of a third-party application accessing APIs through a trusted identity… |
| `time-based-authentication-with-mfa.md` | Time limited authentication with SMS - Twilio Tutorial | Set up time limited authentication with MFA factors such as SMS using Twilio. |
| `time-limited-authentication.md` | Time limited authentication | Support time limited authentication for your ServiceNow instance. |
| `token-based-auth-api.md` | Token-based authentication | Token-based authentication for inbound REST APIs configuration using API Key or HMAC. |
| `token-based-authentication.md` | Token based authentication \(User logins\) | Enhance the security mechanism for users to access a network using token based authentication. |
| `token-expiry-api-and-hmac.md` | Cleaning up token Expiry | Details about how to clean up token expiry by using different system properties. |
| `totp-authenticator-apps.md` | Time-based one-time password \(TOTP\) authentication | A time based one-time password (TOTP) is a secure authentication factor that verifies user identity by generating a unique, time-sensitive… |
| `troubleshoot-mfa-enforcement.md` | Troubleshooting Multi-factor Authentication enforcement | Troubleshooting information due to the MFA enforcement. |
| `troubleshooting-trusted-device.md` | Trusted Mobile app troubleshooting | Review these troubleshooting scenarios to resolve issues with Trusted Mobile app. |
| `unsupported-password-characters.md` | Unsupported password characters | There are password characters that are not supported. Users cannot use these characters, based on ServiceNow password complexity… |
| `use-facebook-based-sso.md` | Use Facebook-based Single Sign-On \(SSO\) | Log in to your ServiceNow instance by using your Facebook credentials on the Facebook-based SSO. |
| `use-idp-filter-criteria-oidc.md` | Use Identity Provider Attribute as Filter Criteria for OIDC | Use the Identity Provider (IDP) attribute from the OpenID Connect (OIDC) response as a filter criteria for authentication policy. |
| `use-idp-filter-criteria.md` | Use Identity Provider Attribute as Filter Criteria for SAML | Use the Identity Provider (IDP) attribute from the Security Assertion Markup Language (SAML) response as a filter criteria for… |
| `use-ip-session-context.md` | Tutorial: Configuring session validation | Configure session validation within the Adaptive Authentication framework to provide as an additional layer of protection for session or… |
| `use-lf-in-mfa.md` | Use Location Filter in MFA Context | Use the location filter criteria created in MFA Context. |
| `use-lf-post-auth.md` | Use Location Filter Post Authentication Context | Use the location filter criteria created in the Post Authentication Context. |
| `use-lf-pre-auth.md` | Use Location Filter in Pre Authentication Context | Use the location filter criteria created in the Pre Authentication Context. |
| `use-location-filter-criteria.md` | Tutorial: Use Location Filter criteria | Describes steps to use location filter criteria in the authentication policy and restrict access to the users based on the location. |
| `user-metrics.md` | User Metrics | User Metrics displays the user MFA enrollment trends on ServiceNow. |
| `user-pub-cred.md` | Configuring Multi-factor Authentication with Biometrics | Administrators can use the User Public Credentials list to view and manager user created credentials. |
| `using-json-web-token-grant.md` | JSON Web token grant workflow | Configuring an OAuth JSON Web Token (JWT) bearer grant secures token-based authentication without user interaction. |
| `verify-user-self-reg-requests.md` | Verify user self-registration requests | After a user registers from the Service Portal , a user record is added to the Registration Requests module. You can view the list of… |
| `view-custom-url-datacenter-jobs.md` | Custom URL datacenter job information | Every custom URL that is associated to your instance has a corresponding ServiceNow datacenter job which runs and shows URL information… |
| `vonage-provider-config.md` | Vonage Provider custom configuration \(Tutorial\) | Configure a SMS with Vonage Provider to ensure every user can login securely. |
| `web-authentication-mfa.md` | Web Authentication - MFA | Use the Integration - Web Authentication (com.snc.integration.webauthn) to allow hardware key or biometric reader authentication on your… |
| `web-embeddables.md` | Web Embeddables | Secure the web embeddables feature for authenticating the ServiceNow's web components that are used in third-party portals. |
| `x-509-certificate-sso.md` | X.509 certificates for SAML | Store and activate the necessary IdP certificates for your SAML configuration. |
