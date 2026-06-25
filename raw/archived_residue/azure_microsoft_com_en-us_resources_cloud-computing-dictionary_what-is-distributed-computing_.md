---
original_url: https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-distributed-computing/
fetched: 2026-05-08
source_tool: curl
---

% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0
  0     0    0     0    0     0      0      0 --:--:--  0:00:02 --:--:--     0
  0     0    0     0    0     0      0      0 --:--:--  0:00:03 --:--:--     0
100 15439    0 15439    0     0   4128      0 --:--:--  0:00:03 --:--:--  4128<!DOCTYPE HTML> <html lang="en-US" dir="ltr"> <head>        <meta charset="UTF-8"/> <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/> <meta http-equiv="x-ua-compatible" content="ie=edge"/> <meta name="content-page-ref" content="oGw4a85CnCDglGADCsJX962OvIIcOKKsp-b-3lrGlJLlrZ_Bbe1lox1tZ5KrjMyC_RP664nV5rTOtW0qEklfAFOgJoLgq1nWkOaP_VW76BzulK7fcAiBXLWBkhO6LqnBlLuCjYM4BdAta6u7u9uZm4YRYezJ86nFgUY2IOKJxdE"/>
<script defer="defer" type="text/javascript" src="https://rum.hlx.page/.rum/@adobe/helix-rum-js@%5E2/dist/micro.js" data-routing="program=147723,environment=1510601,tier=publish"></script>
<link rel="icon" href="/favicon.ico?v2" type="image/x-icon"/> <meta name="robots" content="index, follow"/> <meta name="template" content="reimagine---product-detail-3"/> <meta name="awa-canvasType" content="web"/> <meta name="awa-isTented" content="false"/> <meta name="awa-ver" content="AICC"/> <meta name="awa-pgtmp" content="reimagine---product-detail-3"/> <meta name="awa-pageType" content="Dynamics 365"/> <meta name="awa-market" content="en-us"/> <meta name="awa-cms" content="AEM"/>  <title>What Is Distributed Computing? | Microsoft Azure</title> <link rel="canonical" href="https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-distributed-computing"/> <meta name="description" content="Learn what distributed computing is, how it works, its benefits, and common use cases like cloud services, big data analytics, and scientific research."/> <meta name="twitter:url" content="https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-distributed-computing"/> <meta name="twitter:title" content="What Is Distributed Computing? | Microsoft Azure"/> <meta name="twitter:description" content="Learn what distributed computing is, how it works, its benefits, and common use cases like cloud services, big data analytics, and scientific research."/> <meta name="twitter:card" content="summary"/> <meta property="og:url" content="https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-distributed-computing"/> <meta property="og:title" content="What Is Distributed Computing? | Microsoft Azure"/> <meta property="og:description" content="Learn what distributed computing is, how it works, its benefits, and common use cases like cloud services, big data analytics, and scientific research."/> <meta property="og:type" content="website"/> <meta property="keywords" content="what is distributed computing, distributed computing definition, distributed systems components, distributed computing"/> <meta reimagine-env="golf"/> <meta reimagine-locale="en-US"/> <link rel="stylesheet" href="/acom/etc.clientlibs/cascade.component.authoring/clientlibs/clientlib-reimagineui/foundation/page/default.ACSHASHce4ff551bedcac436ec46ccbba633aef.min.css" type="text/css"> <link rel="stylesheet" href="/acom/etc.clientlibs/cascade.component.authoring/clientlibs/clientlib-reimagineui/foundation/page/web-components.ACSHASH95568bf2884728586b947e1b75640d0e.min.css" type="text/css"> <script src="/acom/etc.clientlibs/cascade.component.authoring/clientlibs/clientlib-reimagine-env/base.ACSHASH8cd32d1ad0be8a1a9b98c8f1eda1aae6.min.js"></script> <link rel="stylesheet" href="/acom/etc.clientlibs/cascade.component.authoring/clientlibs/clientlib-utils/xf-wrapper.ACSHASH959cf4e6c9dbc0269984ead635843b60.min.css" type="text/css"> <link rel="stylesheet" href="/acom/etc.clientlibs/onecloud/clientlibs/clientlib-mwf-new/main-light.ACSHASH561c834597fb9bc5aac4021e21e006be.min.css" type="text/css"> <link rel="stylesheet" href="/acom/etc.clientlibs/onecloud/clientlibs/clientlib-reimagine/main-azure.ACSHASH3ec7f0df3b2a76697fa001237ab044a4.min.css" type="text/css"> <script src="/acom/etc.clientlibs/onecloud/clientlibs/clientlib-vars/publisher.ACSHASHd04116a7de4f2a26cdce768dfe83c5b0.min.js"></script> <script src="/acom/etc.clientlibs/onecloud/clientlibs/clientlib-onecloud-util.ACSHASHe27d1f017cb64db7f5a2a53fe34faf64.min.js"></script> <script src="/acom/etc.clientlibs/onecloud/clientlibs/clientlib-mwf-new/main-light.ACSHASHfe9d5283cc0a38f995b64bf0f39192eb.min.js"></script> <script src="/acom/etc.clientlibs/onecloud/clientlibs/clientlib-reimagine/main-light.ACSHASH4ce28a9a0816fdead46b5df38d680e0d.min.js"></script> <script src="/acom/etc.clientlibs/onecloud/clientlibs/clientlib-events.ACSHASH4c28b55b872280fe389b01920b5c9315.min.js"></script> <link rel="stylesheet" href="/acom/etc.clientlibs/cascade.component.authoring/clientlibs/clientlib-uhf.ACSHASHf9f2395c582fa601707b7a5dfae9f05f.min.css" type="text/css"> <link rel="stylesheet" href="/acom/etc.clientlibs/onecloud/clientlibs/clientlib-action.ACSHASH44700d76f3f63fa33f30039bb9c74b39.min.css" type="text/css"> <link rel="stylesheet" href="/acom/etc.clientlibs/onecloud/clientlibs/clientlib-reimagine-page/clientlib-aem-styles.ACSHASHbf0606832c604770016973857c2f53e8.min.css" type="text/css">  <script>oc.geo.country = "AR";</script>  <script id="ie11-polyfill-script">
        var isModernBrowser = (
            'fetch' in window &&
            'assign' in Object
        );

        if ( !isModernBrowser ) {
            var scriptElement = document.createElement('script');

            scriptElement.async = false;
            scriptElement.src = '/acom/etc.clientlibs/cascade.component.authoring/clientlibs/clientlib-polyfills/resources/ie11-polyfills.js';

            var polyfillScriptElement = document.querySelector('#ie11-polyfill-script');

            if (polyfillScriptElement) {
                polyfillScriptElement.parentNode.insertBefore(scriptElement, polyfillScriptElement.nextSibling);
            }
        }
    </script> <script src="/acom/etc.clientlibs/cascade.component.authoring/clientlibs/clientlib-polyfills.ACSHASHtrue.min.js"></script> <script src="/acom/etc.clientlibs/cascade.component.authoring/clientlibs/clientlib-jquery.ACSHASH75d0cb3e9ff9fee40f5ce5fd93c17fb2.min.js"></script> <script src="/acom/etc.clientlibs/cascade.component.authoring/clientlibs/clientlib-jquery-cookie.ACSHASH5c75a4fa9fb3503322f8a0c9dd51512d.min.js"></script>  <script src="/acom/etc.clientlibs/microsoft/clientlibs/exp-analytics/v1.ACSHASHbf7b336dbb370c984e1bf59b1a980d86.min.js"></script> <script type="text/javascript">
                var expToken = {
                    "exp": {
                        "target": {
                            "propertyToken": "516e8d85-40eb-32f1-cef9-14f2760160a7",
                            "visitorJsHash": "3d099c67f11e65baad62b5d21e36827e",
                            "expJsHash": "e8ee6e3433a60c66439eaf7e8101f8d8",
                            "isExpWithoutPersonalizationEnabled": ("false"==="true")
                        }
                    }
                };
                window.cas = expToken;
            </script> <meta name="cas-exp-visitor" content="/acom/etc.clientlibs/microsoft/components/structure/page/clientlibs/visitor.ACSHASH3d099c67f11e65baad62b5d21e36827e.min.js"> <meta name="cas-exp-at" content="/acom/etc.clientlibs/microsoft/components/structure/page/clientlibs/experimentation.ACSHASHe8ee6e3433a60c66439eaf7e8101f8d8.min.js"> <script type="text/javascript" src="/acom/etc.clientlibs/microsoft/clientlibs/exp-cookiecomp/v1.ACSHASHa238861e6209e4e02576ddf5d1749c8b.min.js" async></script> <meta name="exp-visitor-anchor" content=""/>      <meta name="exp-atjs-anchor" content=""/>  <link id="onecloud-head-style" href="/msonecloudapi/assets/msochead.css" type="text/css" rel="stylesheet"/> <script id="onecloud-head-script" type="text/javascript" src="/msonecloudapi/assets/msochead.js"> </script> <script type="text/javascript" async src="https://play.vidyard.com/embed/v4.js"></script> <script id="oc-cookie-consent-data" type="text/plain">
            
                    {"hasConsent":true,"companyProfile":null,"error":null}
                
        </script> <script id="oc-cookie-consent">
        (function () {
            var defaultConsent = { hasConsent: false };
            window.serverSideConsent = defaultConsent;

            var cookieConsentElement = document.getElementById("oc-cookie-consent-data");
            if (!cookieConsentElement) {
                return;
            }

            var consentText = cookieConsentElement.textContent || cookieConsentElement.innerText;
            if (!consentText) {
                return;
            }

            try {
                var trimmedConsentText = consentText.trim();
                if (!trimmedConsentText) {
                    return;
                }

                var parsedConsent = JSON.parse(trimmedConsentText);
                if (parsedConsent && typeof parsedConsent === "object") {
                    window.serverSideConsent = parsedConsent;
                }
            } catch (error) {
                // Keep defaultConsent on any parsing error
                console.warn("[OneCloud] Error parsing cookie consent data: ", error);
            }
        })();
    </script> <meta name="oc-version" content="reimagine"/> <script src="/acom/etc.clientlibs/cascade.component.authoring/dynamicclientsidelibs/handlerscripts/v1.ACSHASH6734c5d7a732130b83c7d4a6ba54dcec.min.js"></script> <meta name="awa-program" content="acom" /><meta name="awa-enabledFeatures" content="LocaleDetection;QspEnabled;contentbackfillgenerate;esiproductcards;feature-controlled-mwf;uhf-ms-io-endpoint;uhf-esi-cv;uhf-esi-cache;contentsquare;mediapixel;holiday-themer;lazyload-static-components;clientlibDefer;upsellEnabled;contentbackfillpkgdelete;healthcheck;contentbackfillhttpgenerate;perf-tracker-1ds;dynamic-bundle;cvIncrementer;tentingEnabled;chatCookiesImplemented;alertCountDownWithoutServerTime;pdpDynamicRendering;bundlesDynamicRendering;contentbackfillmetadatachangesvideo;contentbackfillmetadatachangesnonvideo;listDynamicRendering;experimentation-without-personalization;generic-list-importer;combinedUHF;cvCallEnabled;m365ProductCatalog;support-unsupported-locales;vsbEnabled;deferClickTale;videoLazyLoad;prefetchFontsEnabled;enable-code-isolation;imageLinkTag;fetchPriority;contentIngestionAgent;enableClickgroupTelemetry;imageLazyLoad;contentIngestionAgent-dispatcher2westus2Agent;isCacheControlFeatureEnabled;feature-controlled-content-card;lcpPrioritizationPhase1;ocReimagineTelemetry;deferScriptsEnabled;lcpPrioritizationPhase2;ocReimagineSlotNumberTelemetry;contentIngestionAgent-dispatcher1westus2Agent;ocReimagineComponentNameTelemetry;ocReimagineTemplateNameTelemetry;ptePhase1;extended-html-minification-sites;dynamicPrice;gl-auto-config;displayV35Toggle;chatCustomEndpoint;enableBoostPersonalization;ocReimagineTelemetryTemplateNameSwap;enableEmailConnector;enable-eventingService;ocReimagineAIAssistant;acsPMEFeatureEnabled;ocReimagineCustomerApiUrl;ocReimagineCustomerFilterApiUrl;email-FigmaEmailAutomation;storeVideoUmp;ocProductPricePrimaryLocale;complianceManagerEnabled;entertainmentEW;enableClarityScript;EnableCascadeAuthSDK;ecsMigrationCheck" />
<script>(window.BOOMR_mq=window.BOOMR_mq||[]).push(["addVar",{"rua.upush":"false","rua.cpush":"false","rua.upre":"false","rua.cpre":"false","rua.uprl":"false","rua.cprl":"false","rua.cprf":"false","rua.trans":"","rua.cook":"false","rua.ims":"false","rua.ufprl":"false","rua.cfprl":"false","rua.isuxp":"false","rua.texp":"norulematch","rua.ceh":"false","rua.ueh":"false","rua.ieh.st":"0"}]);</script>
                                <script>!function(e){var n="https://s.go-mpulse.net/boomerang/";if("False"=="True")e.BOOMR_config=e.BOOMR_config||{},e.BOOMR_config.PageParams=e.BOOMR_config.PageParams||{},e.BOOMR_config.PageParams.pci=!0,n="https://s2.go-mpulse.net/boomerang/";if(window.BOOMR_API_key="E7B88-8P87Z-VT9SJ-BNQSU-2GTUH",function(){function e(){if(!i){var e=document.createElement("script");e.id="boomr-scr-as",e.src=window.BOOMR.url,e.async=!0,o.parentNode.appendChild(e),i=!0}}function t(e){i=!0;var n,t,a,r,d=document,O=window;if(window.BOOMR.snippetMethod=e?"if":"i",t=function(e,n){var t=d.createElement("script");t.id=n||"boomr-if-as",t.src=window.BOOMR.url,BOOMR_lstart=(new Date).getTime(),e=e||d.body,e.appendChild(t)},!window.addEventListener&&window.attachEvent&&navigator.userAgent.match(/MSIE [67]\./))return window.BOOMR.snippetMethod="s",void t(o.parentNode,"boomr-async");a=document.createElement("IFRAME"),a.src="about:blank",a.title="",a.role="presentation",a.loading="eager",r=(a.frameElement||a).style,r.width=0,r.height=0,r.border=0,r.display="none",o.parentNode.appendChild(a);try{O=a.contentWindow,d=O.document.open()}catch(_){n=document.domain,a.src="javascript:var d=document.open();d.domain='"+n+"';void(0);",O=a.contentWindow,d=O.document.open()}if(n)d._boomrl=function(){this.domain=n,t()},d.write("<bo"+"dy onload='document._boomrl();'>");else if(O._boomrl=function(){t()},O.addEventListener)O.addEventListener("load",O._boomrl,!1);else if(O.attachEvent)O.attachEvent("onload",O._boomrl);d.close()}function a(e){window.BOOMR_onload=e&&e.timeStamp||(new Date).getTime()}if(!window.BOOMR||!window.BOOMR.version&&!window.BOOMR.snippetExecuted){window.BOOMR=window.BOOMR||{},window.BOOMR.snippetStart=(new Date).getTime(),window.BOOMR.snippetExecuted=!0,window.BOOMR.snippetVersion=12,window.BOOMR.url=n+"E7B88-8P87Z-VT9SJ-BNQSU-2GTUH";var o=document.currentScript||document.getElementsByTagName("script")[0],i=!1,r=document.createElement("link");if(r.relList&&"function"==typeof r.relList.supports&&r.relList.supports("preload")&&"as"in r)window.BOOMR.snippetMethod="p",r.href=window.BOOMR.url,r.rel="preload",r.as="script",r.addEventListener("load",e),r.addEventListener("error",function(){t(!0)}),setTimeout(function(){if(!i)t(!0)},3e3),BOOMR_lstart=(new Date).getTime(),o.parentNode.appendChild(r);else t(!1);if(window.addEventListener)window.addEventListener("load",a,!1);else if(window.attachEvent)window.attachEvent("onload",a)}}(),"".length>0)if(e&&"performance"in e&&e.performance&&"function"==typeof e.performance.setResourceTimingBufferSize)e.performance.setResourceTimingBufferSize();!function(){if(BOOMR=e.BOOMR||{},BOOMR.plugins=BOOMR.plugins||{},!BOOMR.plugins.AK){var n=""=="true"?1:0,t="",a="aijppmixgo45g2p6d4da-f-99ec4a661-clientnsv4-s.akamaihd.net",o="false"=="true"?2:1,i={"ak.v":"41","ak.cp":"1325064","ak.ai":parseInt("798188",10),"ak.ol":"0","ak.cr":0,"ak.ipv":4,"ak.proto":"http/1.1","ak.rid":"1a05323d","ak.r":45133,"ak.a2":n,"ak.m":"dsca","ak.n":"essl","ak.cport":39782,"ak.gh":"23.192.149.24","ak.quicv":"","ak.tlsv":"tls1.3","ak.0rtt":"","ak.0rtt.ed":"","ak.csrc":"-","ak.acc":"bbr","ak.t":"1778261766","ak.ak":"hOBiQwZUYzCg5VSAfCLimQ==Aag0ffzAr5/BZHjrjaKQ53YTmktj59L7JtF9oKeRtEwUCltM7brhrGTk6gOZgPwzTLTdIVFLWp/8lCLR2S48I+OnZG0d7qBDF2GrQWBBuJTcwXVv3OiKaiCQLd3VfGDbP+croPaXVF+PpN37FFP8ASRUsiMKB1h4BhlnvzFYOEJzgv/iInN7fRHIrTKSl5+DuKkyhglOpSJsW9bQNs4y5caMAEr4Tgmn0gXlG2ru4KLn2S4Jb97q3+Ed97qa2fAW00wGFo5sFsC0Z/jaFZJ6n5WwwrP7FT+WJl+EEn+dB5HKJFptZxujaZabn0J8M54NecZn6Y19/LAzsRM+pC8wZmOjGzzYHYoKNzpjYmtK9gLjmga6YonJk5PLURzWakWuNReSFJb6id4AwjeyYrTqi8ltYFUbFR0pTZkLlSg+Xus=","ak.pv":"125","ak.dpoabenc":"","ak.tf":o};if(""!==t)i["ak.ruds"]=t;var r={i:!1,av:function(n){var t="http.initiator";if(n&&(!n[t]||"spa_hard"===n[t]))i["ak.feo"]=void 0!==e.aFeoApplied?1:0,BOOMR.addVar(i)},rv:function(){var e=["ak.cport","ak.cr","ak.csrc","ak.gh","ak.ipv","ak.m","ak.n","ak.ol","ak.proto","ak.quicv","ak.tlsv","ak.0rtt","ak.0rtt.ed","ak.r","ak.acc","ak.t","ak.tf"];BOOMR.removeVar(e)}};BOOMR.plugins.AK={akVars:i,akDNSPreFetchDomain:a,init:function(){if(!r.i){var e=BOOMR.subscribe;e("before_beacon",r.av,null,null),e("onbeacon",r.rv,null,null),r.i=!0}return this},is_complete:function(){return!0}}}}()}(window);</script></head> <body class="reimagine-page page basicpage">  <div data-geo-country="AR">  <span style="display:none">   <script>
  	  			window.mscv = 'CASMicrosoft0000.0'
  			</script>         <script>
  	  			window.msservercv = 'CASMicrosoftCV1a05323d.0'
  			</script>   This is the Trace Id: 6db960392be4a4d06a3e2711df88296c <script>
					window.traceid = '6db960392be4a4d06a3e2711df88296c'
				</script>  </span> <script type="text/javascript">
		window.msauthIsPublisher = true;
	</script>   <span aria-hidden="true" class="d-none geo-info" data-continent="SA" data-country_code="AR" data-region_code="" data-city="GUALEGUAY" data-timezone="GMT-3" data-zip="" data-county="" data-areacode=""> </span>  <div id="page-top" tabindex="-1"></div> <div id="modalsRenderedAfterPageLoad"> </div> <script type="application/json" id="content-tokens-data">
    {}
  </script> <div class="root responsivegrid"> <div class="aem-Grid aem-Grid--12 aem-Grid--default--12 "> <div class="universalheader aem-GridColumn aem-GridColumn--default--12" data-component-id="cf9a86dceae618e01d6e6399d243873c"> <link rel="stylesheet" href="/acom/etc.clientlibs/microsoft/components/content/universalheader/v1/universalheader/clientlibs/site.ACSHASH56f4647082672f661e4ab78b3e2561e2.min.css" type="text/css">         <link rel="stylesheet" href="https://www.microsoft.com/onerfstatics/marketingsites-eus-prod/west-european/shell/_scrf/css/themes=default.device=uplevel_web_pc/63-57d110/c9-be0100/a6-e969ef/43-9f2e7c/82-8b5456/a0-5d3913/4f-460e79/ae-f1ac0c?ver=2.0&amp;_cf=02242021_3231" type="text/css" media="all" />    <div id="headerArea" class="uhf"  data-m='{"cN":"headerArea","cT":"Area_coreuiArea","id":"a1Body","sN":1,"aN":"Body"}'>
                <div id="headerRegion"      data-region-key="headerregion" data-m='{"cN":"headerRegion","cT":"Region_coreui-region","id":"r1a1","sN":1,"aN":"a1"}' >

    <div  id="headerUniversalHeader" data-m='{"cN":"headerUniversalHeader","cT":"Module_coreui-universalheader","id":"m1r1a1","sN":1,"aN":"r1a1"}'  data-module-id="Category|headerRegion|coreui-region|headerUniversalHeader|coreui-universalheader">
        


                        <div data-m='{"cN":"cookiebanner_cont","cT":"Container","id":"c1m1r1a1","sN":1,"aN":"m1r1a1"}'>

<div id="uhfCookieAlert" data-locale="en-us">
    <div id="msccBannerV2"></div>
</div>

                            
                        </div>




        <a id="uhfSkipToMain" class="m-skip-to-main" href="javascript:void(0)" data-href="#mainContent" tabindex="0" data-m='{"cN":"Skip to content_nonnav","id":"nn2m1r1a1","sN":2,"aN":"m1r1a1"}'>Skip to main content</a>


<header class="c-uhfh context-uhf no-js c-sgl-stck c-category-header " itemscope="itemscope" data-header-footprint="/Azure/AzureHeader, fromService: True"   data-magict="true"   itemtype="http://schema.org/Organization">
    <div class="theme-light js-global-head f-closed  global-head-cont" data-m='{"cN":"Universal Header_cont","cT":"Container","id":"c3m1r1a1","sN":3,"aN":"m1r1a1"}'>
        <div class="c-uhfh-gcontainer-st">
            <button type="button" class="c-action-trigger c-glyph glyph-global-nav-button" aria-label="All Microsoft expand to see list of Microsoft products and services" initialState-label="All Microsoft expand to see list of Microsoft products and services" toggleState-label="Close All Microsoft list" aria-expanded="false" data-m='{"cN":"Mobile menu button_nonnav","id":"nn1c3m1r1a1","sN":1,"aN":"c3m1r1a1"}'></button>
            <button type="button" class="c-action-trigger c-glyph glyph-arrow-htmllegacy c-close-search" aria-label="Close search" aria-expanded="false" data-m='{"cN":"Close Search_nonnav","id":"nn2c3m1r1a1","sN":2,"aN":"c3m1r1a1"}'></button>
                    <a id="uhfLogo" class="c-logo c-sgl-s

... [OUTPUT TRUNCATED - 178772 chars omitted out of 228772 total] ...

ROI from AI_nav","id":"n6c2c1c1m1r1a2","sN":6,"aN":"c2c1c1m1r1a2"}'>Maximize ROI from AI</a>
                            </li>

                        </ul>
                        
                    </div>
                    <div class="c-uhff-nav-group" data-m='{"cN":"footerNavColumn3_cont","cT":"Container","id":"c3c1c1m1r1a2","sN":3,"aN":"c1c1m1r1a2"}'>
                        <div class="c-heading-4" role="heading" aria-level="2">Solutions and support</div>
                        <ul class="c-list f-bare">
                            <li>
                                <a aria-label="Solutions Solutions and support" class="c-uhff-link" href="https://azure.microsoft.com/en-us/solutions/" data-m='{"cN":"Solutions_nav","id":"n1c3c1c1m1r1a2","sN":1,"aN":"c3c1c1m1r1a2"}'>Solutions</a>
                            </li>
                            <li>
                                <a aria-label="Resources for accelerating growth Solutions and support" class="c-uhff-link" href="https://azure.microsoft.com/en-us/solutions/turn-your-vision-into-impact-with-azure/" data-m='{"cN":"Resources for accelerating growth_nav","id":"n2c3c1c1m1r1a2","sN":2,"aN":"c3c1c1m1r1a2"}'>Resources for accelerating growth</a>
                            </li>
                            <li>
                                <a aria-label="Solution architectures Solutions and support" class="c-uhff-link" href="https://learn.microsoft.com/azure/architecture/browse/" data-m='{"cN":"Solution architectures_nav","id":"n3c3c1c1m1r1a2","sN":3,"aN":"c3c1c1m1r1a2"}'>Solution architectures</a>
                            </li>
                            <li>
                                <a aria-label="Support Solutions and support" class="c-uhff-link" href="https://azure.microsoft.com/en-us/support/" data-m='{"cN":"Support_nav","id":"n4c3c1c1m1r1a2","sN":4,"aN":"c3c1c1m1r1a2"}'>Support</a>
                            </li>
                            <li>
                                <a aria-label="Azure demo and live Q&amp;A Solutions and support" class="c-uhff-link" href="https://azure.microsoft.com/en-us/get-started/welcome-to-azure/" data-m='{"cN":"Azure demo and live Q\u0026A_nav","id":"n5c3c1c1m1r1a2","sN":5,"aN":"c3c1c1m1r1a2"}'>Azure demo and live Q&amp;A</a>
                            </li>

                        </ul>
                        
                    </div>
                </div>
                <div class="c-uhff-nav-row">
                    <div class="c-uhff-nav-group" data-m='{"cN":"footerNavColumn4_cont","cT":"Container","id":"c4c1c1m1r1a2","sN":4,"aN":"c1c1m1r1a2"}'>
                        <div class="c-heading-4" role="heading" aria-level="2">Partners</div>
                        <ul class="c-list f-bare">
                            <li>
                                <a aria-label="Software Development Companies Partners" class="c-uhff-link" href="https://www.microsoft.com/en-us/software-development-companies" data-m='{"cN":"Software Development Companies_nav","id":"n1c4c1c1m1r1a2","sN":1,"aN":"c4c1c1m1r1a2"}'>Software Development Companies</a>
                            </li>
                            <li>
                                <a aria-label="Microsoft Marketplace Partners" class="c-uhff-link" href="https://marketplace.microsoft.com/en-us/" data-m='{"cN":"Microsoft Marketplace_nav","id":"n2c4c1c1m1r1a2","sN":2,"aN":"c4c1c1m1r1a2"}'>Microsoft Marketplace</a>
                            </li>
                            <li>
                                <a aria-label="Find a partner Partners" class="c-uhff-link" href="https://azure.microsoft.com/en-us/partners/" data-m='{"cN":"Find a partner_nav","id":"n3c4c1c1m1r1a2","sN":3,"aN":"c4c1c1m1r1a2"}'>Find a partner</a>
                            </li>

                        </ul>
                        
                    </div>
                    <div class="c-uhff-nav-group" data-m='{"cN":"footerNavColumn5_cont","cT":"Container","id":"c5c1c1m1r1a2","sN":5,"aN":"c1c1m1r1a2"}'>
                        <div class="c-heading-4" role="heading" aria-level="2">Resources</div>
                        <ul class="c-list f-bare">
                            <li>
                                <a aria-label="Documentation Resources" class="c-uhff-link" href="https://learn.microsoft.com/en-us/azure/" data-m='{"cN":"Documentation_nav","id":"n1c5c1c1m1r1a2","sN":1,"aN":"c5c1c1m1r1a2"}'>Documentation</a>
                            </li>
                            <li>
                                <a aria-label="Blog Resources" class="c-uhff-link" href="https://azure.microsoft.com/en-us/blog/" data-m='{"cN":"Blog_nav","id":"n2c5c1c1m1r1a2","sN":2,"aN":"c5c1c1m1r1a2"}'>Blog</a>
                            </li>
                            <li>
                                <a aria-label="Developer resources Resources" class="c-uhff-link" href="https://azure.microsoft.com/en-us/resources/developers/" data-m='{"cN":"Developer resources_nav","id":"n3c5c1c1m1r1a2","sN":3,"aN":"c5c1c1m1r1a2"}'>Developer resources</a>
                            </li>
                            <li>
                                <a aria-label="Students Resources" class="c-uhff-link" href="https://azure.microsoft.com/en-us/resources/students/" data-m='{"cN":"Students_nav","id":"n4c5c1c1m1r1a2","sN":4,"aN":"c5c1c1m1r1a2"}'>Students</a>
                            </li>
                            <li>
                                <a aria-label="Events and Webinars Resources" class="c-uhff-link" href="https://azure.microsoft.com/en-us/resources/events/" data-m='{"cN":"Events and Webinars_nav","id":"n5c5c1c1m1r1a2","sN":5,"aN":"c5c1c1m1r1a2"}'>Events and Webinars</a>
                            </li>
                            <li>
                                <a aria-label="Analyst reports, white papers, and e-books Resources" class="c-uhff-link" href="https://azure.microsoft.com/en-us/resources/research/" data-m='{"cN":"Analyst reports, white papers, and e-books_nav","id":"n6c5c1c1m1r1a2","sN":6,"aN":"c5c1c1m1r1a2"}'>Analyst reports, white papers, and e-books</a>
                            </li>
                            <li>
                                <a aria-label="Videos Resources" class="c-uhff-link" href="https://azure.microsoft.com/en-us/resources/videos" data-m='{"cN":"Videos_nav","id":"n7c5c1c1m1r1a2","sN":7,"aN":"c5c1c1m1r1a2"}'>Videos</a>
                            </li>

                        </ul>
                        
                    </div>
                    <div class="c-uhff-nav-group" data-m='{"cN":"footerNavColumn6_cont","cT":"Container","id":"c6c1c1m1r1a2","sN":6,"aN":"c1c1m1r1a2"}'>
                        <div class="c-heading-4" role="heading" aria-level="2">Cloud computing</div>
                        <ul class="c-list f-bare">
                            <li>
                                <a aria-label="What is cloud computing? Cloud computing" class="c-uhff-link" href="https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-cloud-computing/" data-m='{"cN":"What is cloud computing?_nav","id":"n1c6c1c1m1r1a2","sN":1,"aN":"c6c1c1m1r1a2"}'>What is cloud computing?</a>
                            </li>
                            <li>
                                <a aria-label="What is multicloud? Cloud computing" class="c-uhff-link" href="https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-multi-cloud" data-m='{"cN":"What is multicloud?_nav","id":"n2c6c1c1m1r1a2","sN":2,"aN":"c6c1c1m1r1a2"}'>What is multicloud?</a>
                            </li>
                            <li>
                                <a aria-label="What is machine learning? Cloud computing" class="c-uhff-link" href="https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-machine-learning-platform" data-m='{"cN":"What is machine learning?_nav","id":"n3c6c1c1m1r1a2","sN":3,"aN":"c6c1c1m1r1a2"}'>What is machine learning?</a>
                            </li>
                            <li>
                                <a aria-label="What is deep learning? Cloud computing" class="c-uhff-link" href="https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-deep-learning" data-m='{"cN":"What is deep learning?_nav","id":"n4c6c1c1m1r1a2","sN":4,"aN":"c6c1c1m1r1a2"}'>What is deep learning?</a>
                            </li>
                            <li>
                                <a aria-label="What is AIaaS? Cloud computing" class="c-uhff-link" href="https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-aiaas" data-m='{"cN":"What is AIaaS?_nav","id":"n5c6c1c1m1r1a2","sN":5,"aN":"c6c1c1m1r1a2"}'>What is AIaaS?</a>
                            </li>
                            <li>
                                <a aria-label="What are LLMs? Cloud computing" class="c-uhff-link" href="https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-are-large-language-models-llms" data-m='{"cN":"What are LLMs?_nav","id":"n6c6c1c1m1r1a2","sN":6,"aN":"c6c1c1m1r1a2"}'>What are LLMs?</a>
                            </li>
                            <li>
                                <a aria-label="What is a container? Cloud computing" class="c-uhff-link" href="https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-a-container" data-m='{"cN":"What is a container?_nav","id":"n7c6c1c1m1r1a2","sN":7,"aN":"c6c1c1m1r1a2"}'>What is a container?</a>
                            </li>
                            <li>
                                <a aria-label="What is RAG? Cloud computing" class="c-uhff-link" href="https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-retrieval-augmented-generation-rag" data-m='{"cN":"What is RAG?_nav","id":"n8c6c1c1m1r1a2","sN":8,"aN":"c6c1c1m1r1a2"}'>What is RAG?</a>
                            </li>

                        </ul>
                        
                    </div>
                </div>
        </nav>
    <div class="c-uhff-base">
                <a id="locale-picker-link" aria-label="Content Language Selector. Currently set to English (United States)" class="c-uhff-link c-uhff-lang-selector c-glyph glyph-world" href="https://azure.microsoft.com/en-us/locale" data-m='{"cN":"locale_picker(US)_nav","id":"n7c1c1m1r1a2","sN":7,"aN":"c1c1m1r1a2"}'>English (United States)</a>

            <a data-m='{"id":"n8c1c1m1r1a2","sN":8,"aN":"c1c1m1r1a2"}' href="https://aka.ms/yourcaliforniaprivacychoices" class='c-uhff-link c-uhff-ccpa'>
        <svg role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30 14" xml:space="preserve" height="16" width="43">
            <title>Your Privacy Choices Opt-Out Icon</title>
            <path d="M7.4 12.8h6.8l3.1-11.6H7.4C4.2 1.2 1.6 3.8 1.6 7s2.6 5.8 5.8 5.8z" style="fill-rule:evenodd;clip-rule:evenodd;fill:#fff"/>
            <path d="M22.6 0H7.4c-3.9 0-7 3.1-7 7s3.1 7 7 7h15.2c3.9 0 7-3.1 7-7s-3.2-7-7-7zm-21 7c0-3.2 2.6-5.8 5.8-5.8h9.9l-3.1 11.6H7.4c-3.2 0-5.8-2.6-5.8-5.8z" style="fill-rule:evenodd;clip-rule:evenodd;fill:#06f"/>
            <path d="M24.6 4c.2.2.2.6 0 .8L22.5 7l2.2 2.2c.2.2.2.6 0 .8-.2.2-.6.2-.8 0l-2.2-2.2-2.2 2.2c-.2.2-.6.2-.8 0-.2-.2-.2-.6 0-.8L20.8 7l-2.2-2.2c-.2-.2-.2-.6 0-.8.2-.2.6-.2.8 0l2.2 2.2L23.8 4c.2-.2.6-.2.8 0z" style="fill:#fff"/>
            <path d="M12.7 4.1c.2.2.3.6.1.8L8.6 9.8c-.1.1-.2.2-.3.2-.2.1-.5.1-.7-.1L5.4 7.7c-.2-.2-.2-.6 0-.8.2-.2.6-.2.8 0L8 8.6l3.8-4.5c.2-.2.6-.2.9 0z" style="fill:#06f"/>
        </svg>
        <span>Your Privacy Choices</span>
    </a>

        <noscript>
                <a data-m='{"id":"n9c1c1m1r1a2","sN":9,"aN":"c1c1m1r1a2"}' href="https://aka.ms/yourcaliforniaprivacychoices" class='c-uhff-link c-uhff-ccpa'>
        <svg role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30 14" xml:space="preserve" height="16" width="43">
            <title>Your Privacy Choices Opt-Out Icon</title>
            <path d="M7.4 12.8h6.8l3.1-11.6H7.4C4.2 1.2 1.6 3.8 1.6 7s2.6 5.8 5.8 5.8z" style="fill-rule:evenodd;clip-rule:evenodd;fill:#fff"/>
            <path d="M22.6 0H7.4c-3.9 0-7 3.1-7 7s3.1 7 7 7h15.2c3.9 0 7-3.1 7-7s-3.2-7-7-7zm-21 7c0-3.2 2.6-5.8 5.8-5.8h9.9l-3.1 11.6H7.4c-3.2 0-5.8-2.6-5.8-5.8z" style="fill-rule:evenodd;clip-rule:evenodd;fill:#06f"/>
            <path d="M24.6 4c.2.2.2.6 0 .8L22.5 7l2.2 2.2c.2.2.2.6 0 .8-.2.2-.6.2-.8 0l-2.2-2.2-2.2 2.2c-.2.2-.6.2-.8 0-.2-.2-.2-.6 0-.8L20.8 7l-2.2-2.2c-.2-.2-.2-.6 0-.8.2-.2.6-.2.8 0l2.2 2.2L23.8 4c.2-.2.6-.2.8 0z" style="fill:#fff"/>
            <path d="M12.7 4.1c.2.2.3.6.1.8L8.6 9.8c-.1.1-.2.2-.3.2-.2.1-.5.1-.7-.1L5.4 7.7c-.2-.2-.2-.6 0-.8.2-.2.6-.2.8 0L8 8.6l3.8-4.5c.2-.2.6-.2.9 0z" style="fill:#06f"/>
        </svg>
        <span>Your Privacy Choices</span>
    </a>

        </noscript>
            <a data-m='{"id":"n10c1c1m1r1a2","sN":10,"aN":"c1c1m1r1a2"}' href="https://go.microsoft.com/fwlink/?linkid=2259814" class="c-uhff-link c-uhff-consumer">
        <span>Consumer Health Privacy</span>
    </a>

        <nav aria-label="Microsoft corporate links">
            <ul class="c-list f-bare" data-m='{"cN":"Corp links_cont","cT":"Container","id":"c11c1c1m1r1a2","sN":11,"aN":"c1c1m1r1a2"}'>
                                <li  id="c-uhff-footer_sitemap">
                    <a class="c-uhff-link" href="https://www.microsoft.com/en-us/sitemap1.aspx" data-mscc-ic="false" data-m='{"cN":"Footer_Sitemap_nav","id":"n1c11c1c1m1r1a2","sN":1,"aN":"c11c1c1m1r1a2"}'>Sitemap</a>
                </li>
                <li  id="c-uhff-footer_contactus">
                    <a class="c-uhff-link" href="https://support.microsoft.com/contactus" data-mscc-ic="false" data-m='{"cN":"Footer_ContactUs_nav","id":"n2c11c1c1m1r1a2","sN":2,"aN":"c11c1c1m1r1a2"}'>Contact Microsoft</a>
                </li>
                <li  id="c-uhff-footer_privacyandcookies">
                    <a class="c-uhff-link" href="https://go.microsoft.com/fwlink/?LinkId=521839" data-mscc-ic="false" data-m='{"cN":"Footer_PrivacyandCookies_nav","id":"n3c11c1c1m1r1a2","sN":3,"aN":"c11c1c1m1r1a2"}'>Privacy </a>
                </li>
                <li class=" x-hidden" id="c-uhff-footer_managecookies">
                    <a class="c-uhff-link" href="#" data-mscc-ic="false" data-m='{"cN":"Footer_ManageCookies_nav","id":"n4c11c1c1m1r1a2","sN":4,"aN":"c11c1c1m1r1a2"}'>Manage cookies</a>
                </li>
                <li  id="c-uhff-footer_termsofuse">
                    <a class="c-uhff-link" href="https://go.microsoft.com/fwlink/?LinkID=206977" 
100  222k    0  222k    0     0  59469      0 --:--:--  0:00:03 --:--:-- 59462
data-mscc-ic="false" data-m='{"cN":"Footer_TermsOfUse_nav","id":"n5c11c1c1m1r1a2","sN":5,"aN":"c11c1c1m1r1a2"}'>Terms of use</a>
                </li>
                <li  id="c-uhff-footer_trademarks">
                    <a class="c-uhff-link" href="https://go.microsoft.com/fwlink/?linkid=2196228" data-mscc-ic="false" data-m='{"cN":"Footer_Trademarks_nav","id":"n6c11c1c1m1r1a2","sN":6,"aN":"c11c1c1m1r1a2"}'>Trademarks</a>
                </li>
                <li  id="c-uhff-footer_safetyandeco">
                    <a class="c-uhff-link" href="https://go.microsoft.com/fwlink/?linkid=2196227" data-mscc-ic="false" data-m='{"cN":"Footer_SafetyAndEco_nav","id":"n7c11c1c1m1r1a2","sN":7,"aN":"c11c1c1m1r1a2"}'>Safety &amp; eco</a>
                </li>
                <li  id="c-uhff-recycling">
                    <a class="c-uhff-link" href="https://www.microsoft.com/en-us/legal/compliance/recycling" data-mscc-ic="false" data-m='{"cN":"Recycling_nav","id":"n8c11c1c1m1r1a2","sN":8,"aN":"c11c1c1m1r1a2"}'>Recycling</a>
                </li>
                <li  id="c-uhff-footer_aboutourads">
                    <a class="c-uhff-link" href="https://choice.microsoft.com" data-mscc-ic="false" data-m='{"cN":"Footer_AboutourAds_nav","id":"n9c11c1c1m1r1a2","sN":9,"aN":"c11c1c1m1r1a2"}'>About our ads</a>
                </li>

                <li>&#169; Microsoft 2026</li>
                
            </ul>
        </nav>
        
    </div>
    
</footer>

<script id="uhf-footer-ccpa">
    const globalPrivacyControlEnabled = navigator.globalPrivacyControl;

    const GPC_DataSharingOptIn = (globalPrivacyControlEnabled) ? false : checkThirdPartyAdsOptOutCookie();

    if(window.onGPCLoaded) {
        window.onGPCLoaded();
    }
    
    function checkThirdPartyAdsOptOutCookie() {
        try {
            const ThirdPartyAdsOptOutCookieName = '3PAdsOptOut';
            var cookieValue = getCookie(ThirdPartyAdsOptOutCookieName);
            return cookieValue != 1;
        } catch {
            return true;
        }
    }

    function getCookie(cookieName) {
        var cookieValue = document.cookie.match('(^|;)\\s*' + cookieName + '\\s*=\\s*([^;]+)');
        return (cookieValue) ? cookieValue[2] : '';
    }
</script>







    </div>
        </div>

    </div>
<script src="https://wcpstatic.microsoft.com/mscc/lib/v2/wcp-consent.js"></script><script src="https://www.microsoft.com/onerfstatics/marketingsites-eus-prod/shell/_scrf/js/themes=default/54-af9f9f/fb-2be034/21-f9d187/b0-50721e/d8-97d509/40-0bd7f9/ea-f1669e/9d-c6ea39/62-a72447/3e-a4ee50/7c-0bd6a1/60-37309a/db-bc0148/dc-7e9864/6d-c07ea1/6f-dafe8c/f6-aa5278/e6-5f3533/6d-1e7ed0/b7-cadaa7/62-2741f0/ca-40b7b0/4e-ee3a55/3e-f5c39b/c3-6454d7/f9-7592d3/d0-e64f3e/92-10345d/79-499886/7e-cda2d3/e7-1fe854/66-9d711a/38-b93a9e/de-884374/1f-100dea/33-abe4df/8f-61bee0?ver=2.0&_cf=02242021_3231&iife=1"></script>  </div> </div> </div> <link rel="stylesheet" href="/acom/etc.clientlibs/onecloud/clientlibs/reimagine/clientlib-reimagine-base.ACSHASH81b1ef0c4a6b80454291234fcd6e45b0.min.css" type="text/css"> <link rel="stylesheet" href="/acom/etc.clientlibs/cascade.component.authoring/clientlibs/clientlib-reimagine-base.ACSHASH81b1ef0c4a6b80454291234fcd6e45b0.min.css" type="text/css"> <script src="/acom/etc.clientlibs/onecloud/clientlibs/reimagine/clientlib-reimagine-base.ACSHASHf41d97440f6fa5cbbebf0321d674529b.min.js"></script> <script src="/acom/etc.clientlibs/cascade.component.authoring/clientlibs/clientlib-reimagine-base.ACSHASH2b143bed0ff34bc70bc0703346f70e08.min.js"></script> <script src="/acom/etc.clientlibs/onecloud/clientlibs/clientlib-click-group-telemetry.ACSHASHf25fec6821f63d701a6b6291a4011894.min.js"></script> <script src="/acom/etc.clientlibs/microsoft/clientlibs/clientlib-httpclient.ACSHASHbdf4e043fe12e5b0add3f5e1e82ea4c5.min.js"></script> <script src="/acom/etc.clientlibs/cascade.component.authoring/clientlibs/clientlib-cookieconsent.ACSHASHc892f451b0c4db9c8ab2601a427c9b2c.min.js"></script> <script src="/acom/etc.clientlibs/onecloud/clientlibs/clientlib-cookievalidator.ACSHASH76e71242540c0cc57446a6ee16fe9f52.min.js"></script> <script src="/acom/etc.clientlibs/microsoft/components/structure/page/clientlibs/featurecontrol.ACSHASHf120033122e43a4cb0b53bb306afc5dc.min.js"></script> <div id='customFeatureControl' enabledFeatures="contentbackfillgenerate,esiproductcards,feature-controlled-mwf,uhf-ms-io-endpoint,uhf-esi-cv,uhf-esi-cache,contentsquare,mediapixel,holiday-themer,lazyload-static-components,clientlibDefer,upsellEnabled,contentbackfillpkgdelete,healthcheck,contentbackfillhttpgenerate,perf-tracker-1ds,dynamic-bundle,cvIncrementer,tentingEnabled,chatCookiesImplemented,alertCountDownWithoutServerTime,pdpDynamicRendering,bundlesDynamicRendering,contentbackfillmetadatachangesvideo,contentbackfillmetadatachangesnonvideo,listDynamicRendering,experimentation-without-personalization,generic-list-importer,combinedUHF,cvCallEnabled,m365ProductCatalog,support-unsupported-locales,vsbEnabled,deferClickTale,videoLazyLoad,prefetchFontsEnabled,enable-code-isolation,imageLinkTag,fetchPriority,contentIngestionAgent,enableClickgroupTelemetry,imageLazyLoad,contentIngestionAgent-dispatcher2westus2Agent,isCacheControlFeatureEnabled,feature-controlled-content-card,lcpPrioritizationPhase1,ocReimagineTelemetry,deferScriptsEnabled,lcpPrioritizationPhase2,ocReimagineSlotNumberTelemetry,contentIngestionAgent-dispatcher1westus2Agent,ocReimagineComponentNameTelemetry,ocReimagineTemplateNameTelemetry,ptePhase1,extended-html-minification-sites,dynamicPrice,gl-auto-config,displayV35Toggle,chatCustomEndpoint,enableBoostPersonalization,ocReimagineTelemetryTemplateNameSwap,enableEmailConnector,enable-eventingService,ocReimagineAIAssistant,acsPMEFeatureEnabled,ocReimagineCustomerApiUrl,ocReimagineCustomerFilterApiUrl,email-FigmaEmailAutomation,storeVideoUmp,ocProductPricePrimaryLocale,complianceManagerEnabled,entertainmentEW,enableClarityScript,EnableCascadeAuthSDK,ecsMigrationCheck"></div> <div class='oneds-config' data-instrumentationkey='c72e6b24df604532a6282edd268b4ba4-9cdee1fe-5d2f-4626-9620-dbad9b53a8e5-8065' data-isenabled='true' data-env='prod' data-market='en-us' data-pageName='What Is Distributed Computing? | Microsoft Azure' data-urlCollectQuery='true' data-urlCollectHash='false' data-autoCapturelineage='false' data-autoCaptureresize='false' data-autoCapturescroll='false' data-initialize1DSEventName="none" data-tenantName='acom' data-tenantTitle='Azure.com' data-tenantDomain='azure' data-tenantSiteName='microsoft' data-tenantNameProperty='tenantName' data-tenantTitleProperty='tenantTitle' data-tenantDomainProperty='tenantDomain' data-tenantSiteNameProperty='tenantSiteName' data-max1DSInitializeDelayInSeconds='1'> </div> <script src="/acom/etc.clientlibs/microsoft/components/structure/page/clientlibs/custom-oneds.ACSHASHbf880242325f20f5b8644293f4586135.min.js"></script> <script src="/acom/etc.clientlibs/microsoft/clientlibs/cookie-compliance-manager.ACSHASHd471cafc5d23f4577f5cf2676dcc276a.min.js"></script> <script id="onecloud-body-script" type="text/javascript" src="/msonecloudapi/assets/msocbody.js" async></script> <link rel="stylesheet" href="/acom/etc.clientlibs/onecloud/clientlibs/clientlib-chat.ACSHASHfa6f56b2d3037982772378233706c9af.min.css" type="text/css"> <meta name="chat-default-config" value='{&#34;checkForAgentAvailability&#34;:&#34;false&#34;,&#34;srcFmt&#34;:&#34;https://publisher.liveperson.net/iframe-le-tag/iframe-cs.html?lpsite={0}&amp;lpsection={1}&amp;buttons=hiddenchat&#34;,&#34;telemetryMapping&#34;:&#34;{\&#34;Start\&#34;: [180, \&#34;initiate-chat\&#34;],\&#34;Yes\&#34;: [181, \&#34;end-chat\&#34;],\&#34;options rendered\&#34;: [0, \&#34;display-options\&#34;]}&#34;,&#34;geoExclusion&#34;:&#34;inherit&#34;,&#34;innerContainerId&#34;:&#34;lp-iframe-container&#34;,&#34;siteId&#34;:&#34;60270350&#34;,&#34;topic&#34;:&#34;Office365&#34;,&#34;suppressProactive&#34;:&#34;false&#34;,&#34;domainUrl&#34;:&#34;https://publisher.liveperson.net&#34;}'/> <meta name="chat-default-locale-chat" value="{&#34;market&#34;:&#34;en-us&#34;,&#34;checkForAgentAvailability&#34;:&#34;false&#34;,&#34;suppressProactive&#34;:&#34;false&#34;}"/> <meta name="chat-default-site-type-chat" value="{&#34;checkForAgentAvailability&#34;:&#34;false&#34;,&#34;srcFmt&#34;:&#34;https://publisher.liveperson.net/iframe-le-tag/iframe-cs.html?lpsite={0}&amp;lpsection={1}&amp;buttons=lpChatAzure&#34;,&#34;suppressProactive&#34;:&#34;false&#34;,&#34;sectionId&#34;:&#34;azure-leadgen-{0}&#34;}"/> <meta name="chat-specific-site-type-locale-chat" value="{}"/> <meta name="chat-invite-template" value='&lt;style> #chatEngagement { color: #fff; background-color: #006abb; border: 1px solid #0078d4; border-radius: 4px; display: inline-block; font-size: 14px; font-weight: 600; padding: 10px 16px; } #chatEngagement:hover, #chatEngagement:active { text-decoration: underline; } #chatDisengagement { color: #0062ad; display: inline-block; font-size: 14px; font-weight: 600; padding-right: 1em; position: relative; text-decoration: none; border: none; background-color: transparent; } #chatEngagement:focus { outline: 1px solid #fff; outline-offset: -4px; text-decoration: underline; } #chatDisengagement:after { background-image: url(&#34;data:image/svg+xml,%3Csvg viewBox=&#39;0 0 12 12&#39; fill=&#39;none&#39; xmlns=&#39;http://www.w3.org/2000/svg&#39;%3E%3Cpath d=&#39;M4 1L9 6L4 11&#39; stroke=&#39;%230062ad&#39;/%3E%3C/svg%3E&#34;); content: &#39; &#39;; height: 12px; width: 12px; display: inline-flex; vertical-align: middle; margin-left: .2em; transition: all .2s ease-in-out; position: absolute; bottom: -6px; background-color: transparent; } #chatDisengagement:focus { outline-offset: 10px; } #lp-iframe-container { border: 0; bottom: 0; box-shadow: 0 5px 15px 0 #00000033; height: 500px; left: auto !important; min-width: 300px; max-width: 350px; padding: 0; position: fixed; right: 0; top: auto !important; z-index: 1031; } #iFrame { height: 100%; width: 100%; border: 0; } #proactive-chat-dialog { position: fixed; z-index: 10400; bottom: -24px; right: 11px; } #proactive-chat-dialog .chatContainer { min-width: 272px; height: 277px; color: #000; line-height: 0; position: relative; border: 0 !important; background-repeat: no-repeat !important; background-color: #fff !important; margin: auto; padding: 12px; background-size: contain !important; box-shadow: 0 2.8px 2.2px rgba(0, 0, 0, 0.034), 0 6.7px 5.3px rgba(0, 0, 0, 0.048), 0 12.5px 10px rgba(0, 0, 0, 0.06), 0 22.3px 17.9px rgba(0, 0, 0, 0.072), 0 41.8px 33.4px rgba(0, 0, 0, 0.086), 0 100px 80px rgba(0, 0, 0, 0.12); } #proactive-chat-dialog .chatContainer .chat-cta { text-align: center; font-size: 24px; font-weight: 600; position: relative; top: 160px; } #proactive-chat-dialog .chatContainer .chat-buttons { position: relative; top: 185px; width: 100%; display: flex; gap: 1em; justify-content: center; flex-direction: column; } #proactive-chat-dialog .chatContainer .chat-buttons .arrow-link { width: auto; margin: auto; } #proactive-chat-dialog .chatContainer .chat-buttons .arrow-link:after { bottom: -6px; } @media only screen and (min-width: 33.75em) { #proactive-chat-dialog .chatContainer .chat-buttons { top: 200px; flex-direction: row; } } &lt;/style> &lt;div id=&#34;proactive-chat-dialog&#34; class=&#34;proactive-chat-hidden&#34;> &lt;div class=&#34;chatContainer&#34; style=&#34;background: url(&#39;{{module.bg-img-src}}&#39;) no-repeat top left&#34; > &lt;div class=&#34;chat-cta&#34;>{{module.heading}}&lt;/div> &lt;div class=&#34;chat-buttons&#34;> &lt;button type=&#34;button&#34; id=&#34;chatEngagement&#34; aria-label=&#34;{{chat-engagement.aria-label}}&#34; class=&#34;button button--primary01 lp-chatnow&#34; data-lp-event=&#34;click&#34; data-bi-id=&#34;expand-chat&#34; data-bi-an=&#34;chat&#34; data-bi-chtid=&#34;azure chat 1&#34; data-bi-chtnm=&#34;live person proactive chat&#34; data-bi-bhvr=&#34;16&#34; data-bi-tn=&#34;button button--primary01 lp-chatnow&#34; > {{chat-engagement.btn-txt}} &lt;/button> &lt;button type=&#34;button&#34; id=&#34;chatDisengagement&#34; aria-label=&#34;{{chat-disengagement.aria-label}}&#34; class=&#34;arrow-link lp-nothanks&#34; data-lp-event=&#34;close&#34; data-bi-id=&#34;collapse-chat&#34; data-bi-an=&#34;chat&#34; data-bi-chtid=&#34;azure chat 1&#34; data-bi-chtnm=&#34;live person proactive chat&#34; data-bi-tn=&#34;arrow-link lp-nothanks&#34; > {{chat-disengagement.btn-txt}} &lt;/button> &lt;/div> &lt;/div> &lt;/div> '/> <meta name="chat-invite-fallback-content" value="{ &#34;module&#34;: { &#34;heading&#34;: &#34;Can we help you?&#34;, &#34;bg-img-src&#34;: &#34;https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/north-america&#34; }, &#34;chat-engagement&#34;: { &#34;aria-label&#34;: &#34;Would you like to chat? Click here!&#34;, &#34;btn-txt&#34;: &#34;Chat now&#34; }, &#34;chat-disengagement&#34;: { &#34;aria-label&#34;: &#34;No thanks, close the chat invite&#34;, &#34;btn-txt&#34;: &#34;No thanks&#34; } } "/> <meta name="chat-oc-opts" value='{"chatDialogDescription": "chat with Sales window", "isChatDisabled": "", "siteType": "acom", "disableProactiveChat": "false", "debugHostNames": ["localhost", "sites-author.adobeppe.microsoft.com"]}'/> <script src="/acom/etc.clientlibs/onecloud/clientlibs/clientlib-chat.ACSHASHb21767ddb88a6a72011a1e8a790118f8.min.js"></script> <script src="/acom/etc.clientlibs/cascade.component.authoring/clientlibs/clientlib-reimagine-env/publisher.ACSHASHcd629aed3cfa3b0e32904897f5959c98.min.js"></script> <script src="/acom/etc.clientlibs/cascade.component.authoring/clientlibs/clientlib-reimagine-utils.ACSHASH2e8da8c9230bc7589ee557f90d9f8431.min.js"></script> <script src="/acom/etc.clientlibs/cascade.component.authoring/clientlibs/clientlib-reimagine-telemetry.ACSHASH4954ace0a36fba9801f5284efe99e42c.min.js"></script> <script src="/acom/etc.clientlibs/cascade.component.authoring/clientlibs/clientlib-reimagine-csp.ACSHASHd96f33132be65b878f1461ed46629ec7.min.js"></script> <span hidden data-rds-csp-content></span> <script src="/acom/etc.clientlibs/cascade.component.authoring/clientlibs/clientlib-reimagineui/web-components/inline-price/v1.ACSHASH476f794cde555d7558f19d559119d967.min.js" type="module"></script> <link rel="stylesheet" href="/acom/etc.clientlibs/cascade.component.authoring/clientlibs/clientlib-utils/inline-price.ACSHASH4f33c56ca437d2f1e3132d6f888f400c.min.css" type="text/css"> <div id="web-ai-assistant-experience"> <script src="https://www.microsoft.com/fe/static/feature-evaluator-v2.js" data-endpoint="https://www.microsoft.com/fe/api/features/variants" async></script> <div id="waaModern"> <script type="module" src="https://www.microsoft.com/webassistant/v1/uca.mjs"></script> <div id="unified-chat-assistant" options="{&#34;mode&#34;:&#34;drawer&#34;,&#34;theme&#34;:&#34;theme-day&#34;,&#34;partnerId&#34;:&#34;3237876c-9234-447f-987c-559ac6194158&#34;}"></div> </div> </div> <link rel="stylesheet" href="/acom/etc.clientlibs/onecloud/clientlibs/clientlib-waa-send-prompt.ACSHASH98f9e452c295c1ac0782b6d81f5e5c7f.min.css" type="text/css"> <script src="/acom/etc.clientlibs/onecloud/clientlibs/clientlib-waa-send-prompt.ACSHASH59a26d2047110a73968d71c0988c00a8.min.js"></script> </div> </body> </html>