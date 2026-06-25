---
original_url: https://cloud.google.com/architecture/distributed-systems-concepts
fetched: 2026-05-08
source_tool: curl
---

% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0100   329  100   329    0     0    737      0 --:--:-- --:--:-- --:--:--   737
  9 74622    9  6843    0     0   6460      0  0:00:11  0:00:01  0:00:10  6460








<!doctype html>
<html 
      lang="en"
      dir="ltr">
  <head>
    <meta name="google-signin-client-id" content="721724668570-nbkv1cfusk7kk4eni4pjvepaus73b13t.apps.googleusercontent.com"><meta name="google-signin-scope"
          content="profile email https://www.googleapis.com/auth/developerprofiles https://www.googleapis.com/auth/developerprofiles.award https://www.googleapis.com/auth/devprofiles.full_control.firstparty"><meta property="og:site_name" content="Google Cloud Documentation">
    <meta property="og:type" content="website"><meta name="robots" content="noindex"><meta name="theme-color" content="#1a73e8"><meta charset="utf-8">
    <meta content="IE=Edge" http-equiv="X-UA-Compatible">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    

    <link rel="manifest" href="/_pwa/clouddocs/manifest.json"
          crossorigin="use-credentials">
    <link rel="preconnect" href="//www.gstatic.com" crossorigin>
    <link rel="preconnect" href="//fonts.googleapis.com" crossorigin>
    <link rel="preconnect" href="//www.google-analytics.com" crossorigin><link rel="stylesheet" href="//fonts.googleapis.com/css?family=Google+Sans:400,500|Roboto:400,400italic,500,500italic,700,700italic|Roboto+Mono:400,500,700&display=swap">
      <link rel="stylesheet"
            href="//fonts.googleapis.com/css2?family=Material+Icons&family=Material+Symbols+Outlined&display=block"><link rel="stylesheet" href="https://www.gstatic.com/devrel-devsite/prod/v1b953b434e2033f0160fd97c99360ee5d4d0a613449c2a694360a72d378b9d8e/clouddocs/css/app.css">
      
        <link rel="stylesheet" href="https://www.gstatic.com/devrel-devsite/prod/v1b953b434e2033f0160fd97c99360ee5d4d0a613449c2a694360a72d378b9d8e/clouddocs/css/dark-theme.css" disabled>
      <link rel="shortcut icon" href="https://www.gstatic.com/devrel-devsite/prod/v1b953b434e2033f0160fd97c99360ee5d4d0a613449c2a694360a72d378b9d8e/clouddocs/images/favicons/onecloud/favicon.ico">
    <link rel="apple-touch-icon" href="https://www.gstatic.com/devrel-devsite/prod/v1b953b434e2033f0160fd97c99360ee5d4d0a613449c2a694360a72d378b9d8e/clouddocs/images/favicons/onecloud/super_cloud.png"><link rel="canonical" href="https://docs.cloud.google.com/architecture/distributed-systems-concepts"><link rel="search" type="application/opensearchdescription+xml"
            title="Google Cloud Documentation" href="https://docs.cloud.google.com/s/opensearch.xml">
      <title>404 &nbsp;|&nbsp; Page Not Found &nbsp;|&nbsp; Google Cloud Documentation</title>

<meta property="og:title" content="404 &nbsp;|&nbsp; Page Not Found &nbsp;|&nbsp; Google Cloud Documentation"><meta property="og:image" content="https://docs.cloud.google.com/_static/cloud/images/social-icon-google-cloud-1200-630.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">
    </head>
  <body class="color-scheme--light"
        template="404"
        theme="clouddocs-theme"
        type="error"
        
        appearance
        
        layout="full"
        
        
        free-trial
        
        
        
        pending>
  
    <devsite-progress type="indeterminate" id="app-progress"></devsite-progress>
  
  
    <a href="#main-content" class="skip-link button">
      
      Skip to main content
    </a>
    <section class="devsite-wrapper">
      <devsite-cookie-notification-bar></devsite-cookie-notification-bar>
        <cloudx-track userCountry="AR"></cloudx-track>

<devsite-header role="banner" keep-tabs-visible>
  
    





















<div class="devsite-header--inner" data-nosnippet>
  <div class="devsite-top-logo-row-wrapper-wrapper">
    <div class="devsite-top-logo-row-wrapper">
      <div class="devsite-top-logo-row">
        <button type="button" id="devsite-hamburger-menu"
          class="devsite-header-icon-button button-flat material-icons gc-analytics-event"
          data-category="Site-Wide Custom Events"
          data-label="Navigation menu button"
          visually-hidden
          aria-label="Open menu">
        </button>
        
<div class="devsite-product-name-wrapper">

  <a href="/" class="devsite-site-logo-link gc-analytics-event"
   data-category="Site-Wide Custom Events" data-label="Site logo" track-type="globalNav"
   track-name="googleCloudDocumentation" track-metadata-position="nav"
   track-metadata-eventDetail="nav">
  
  <picture>
    
    <source srcset="https://www.gstatic.com/devrel-devsite/prod/v1b953b434e2033f0160fd97c99360ee5d4d0a613449c2a694360a72d378b9d8e/clouddocs/images/lockup-dark-theme.svg"
            media="(prefers-color-scheme: dark)"
            class="devsite-dark-theme">
    
    <img src="https://www.gstatic.com/devrel-devsite/prod/v1b953b434e2033f0160fd97c99360ee5d4d0a613449c2a694360a72d378b9d8e/clouddocs/images/lockup.svg" class="devsite-site-logo" alt="Google Cloud Documentation">
  </picture>
  
</a>



</div>
        <div class="devsite-top-logo-row-middle">
          <div class="devsite-header-upper-tabs">
            
              
              
  <devsite-tabs class="upper-tabs">

    <nav class="devsite-tabs-wrapper" aria-label="Upper tabs">
      
        
          <tab class="devsite-dropdown
    
    
    devsite-clickable
    ">
  
    <a href="https://docs.cloud.google.com/docs"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://docs.cloud.google.com/docs"
    
       track-type="nav"
       track-metadata-position="nav - docs-home"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Technology areas"
         
           track-name="docs-home"
         
           track-link-column-type="single-column"
         
       >
    Technology areas
  
    </a>
    
      <button
         aria-haspopup="menu"
         aria-expanded="false"
         aria-label="Dropdown menu for Technology areas"
         track-type="nav"
         track-metadata-eventdetail="https://docs.cloud.google.com/docs"
         track-metadata-position="nav - docs-home"
         track-metadata-module="primary nav"
         
          
            data-category="Site-Wide Custom Events"
          
            data-label="Tab: Technology areas"
          
            track-name="docs-home"
          
            track-link-column-type="single-column"
          
        
         class="devsite-tabs-dropdown-toggle devsite-icon devsite-icon-arrow-drop-down"></button>
    
  
  <div class="devsite-tabs-dropdown" role="menu" aria-label="submenu" hidden>
    <div class="devsite-tabs-dropdown-content">
      
        <button class="devsite-tabs-close-button material-icons button-flat gc-analytics-event"
                data-category="Site-Wide Custom Events"
                data-label="Close dropdown menu"
                aria-label="Close dropdown menu"
                track-type="nav"
                track-name="close"
                track-metadata-eventdetail="#"
                track-metadata-position="nav - docs-home"
                track-metadata-module="tertiary nav">close</button>
      
      
        <div class="devsite-tabs-dropdown-column
                    ">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
              
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/ai-ml"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/ai-ml"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      AI and ML
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/application-development"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/application-development"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Application development
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/application-hosting"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/application-hosting"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Application hosting
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/compute-area"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/compute-area"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Compute
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/data"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/data"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Data analytics and pipelines
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/databases"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/databases"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Databases
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/dhm-cloud"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/dhm-cloud"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Distributed, hybrid, and multicloud
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/industry"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/industry"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Industry solutions
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/migration"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/migration"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Migration
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/networking"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/networking"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Networking
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/observability"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/observability"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Observability and monitoring
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/security"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/security"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Security
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/storage"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/storage"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Storage
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
    </div>
  </div>
</tab>
        
      
        
          <tab class="devsite-dropdown
    
    
    devsite-clickable
    ">
  
    <a href="https://docs.cloud.google.com/docs/cross-product-overviews"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://docs.cloud.google.com/docs/cross-product-overviews"
    
       track-type="nav"
       track-metadata-position="nav - crossproduct"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Cross-product tools"
         
           track-name="crossproduct"
         
           track-link-column-type="single-column"
         
       >
    Cross-product tools
  
    </a>
    
      <button
         aria-haspopup="menu"
         aria-expanded="false"
         aria-label="Dropdown menu for Cross-product tools"
         track-type="nav"
         track-metadata-eventdetail="https://docs.cloud.google.com/docs/cross-product-overviews"
         track-metadata-position="nav - crossproduct"
         track-metadata-module="primary nav"
         
          
            data-category="Site-Wide Custom Events"
          
            data-label="Tab: Cross-product tools"
          
            track-name="crossproduct"
          
            track-link-column-type="single-column"
          
        
         class="devsite-tabs-dropdown-toggle devsite-icon devsite-icon-arrow-drop-down"></button>
    
  
  <div class="devsite-tabs-dropdown" role="menu" aria-label="submenu" hidden>
    <div class="devsite-tabs-dropdown-content">
      
        <button class="devsite-tabs-close-button material-icons button-flat gc-analytics-event"
                data-category="Site-Wide Custom Events"
                data-label="Close dropdown menu"
                aria-label="Close dropdown menu"
                track-type="nav"
                track-name="close"
                track-metadata-eventdetail="#"
                track-metadata-position="nav - crossproduct"
                track-metadata-module="tertiary nav">close</button>
      
      
        <div class="devsite-tabs-dropdown-column
                    ">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
              
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/access-resources"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/access-resources"
                     track-metadata-position="nav - crossproduct"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Access and resources management
                    </div>
                 

... [OUTPUT TRUNCATED - 25117 chars omitted out of 75117 total] ...


          aria-haspopup="listbox"
          autocomplete="off"
          class="devsite-search-field devsite-search-query"
          name="q"
          
          placeholder="Search"
          role="combobox"
          type="text"
          value=""
          >
          <div class="devsite-search-image material-icons" aria-hidden="true">
            
          </div>
          <div class="devsite-search-shortcut-icon-container" aria-hidden="true">
            <kbd class="devsite-search-shortcut-icon">/</kbd>
          </div>
      </div>
    </div>
  </form>
  <button type="button"
          search-close
          class="devsite-search-button devsite-header-icon-button button-flat material-icons"
          
          aria-label="Close search"></button>
</devsite-search>

        
      </div>
    
    </div><div class="devsite-floating-action-buttons"></div></article>
</article>
            
          </devsite-content>
        </main>
        <devsite-footer-promos class="devsite-footer">
          
            
          
        </devsite-footer-promos>
        <devsite-footer-linkboxes class="devsite-footer">
          
            
<nav class="devsite-footer-linkboxes nocontent"
     aria-label="Footer links"
     data-nosnippet>
  
  <ul class="devsite-footer-linkboxes-list">
    
    <li class="devsite-footer-linkbox ">
    <h3 class="devsite-footer-linkbox-heading no-link">Products and pricing</h3>
      <ul class="devsite-footer-linkbox-list">
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/products/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 1)"
            track-metadata-position="footer"track-metadata-eventDetail="cloud.google.com/products/"track-name="see all products"track-type="footer link"track-metadata-child_headline="products and pricing"track-metadata-module="footer">
            
          
            See all products
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/pricing/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            track-metadata-position="footer"track-type="footer link"track-metadata-module="footer"track-metadata-child_headline="products and pricing"track-metadata-eventDetail="cloud.google.com/pricing/"track-name="google cloud pricing">
            
          
            Google Cloud pricing
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/marketplace/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            track-type="footer link"track-metadata-child_headline="resources"track-metadata-module="footer"track-metadata-eventDetail="cloud.google.com/marketplace/"track-name="google cloud marketplace"track-metadata-position="footer">
            
          
            Google Cloud Marketplace
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/contact/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            track-metadata-eventDetail="cloud.google.com/contact/"track-name="contact sales"track-type="footer link"track-metadata-module="footer"track-metadata-child_headline="engage"track-metadata-position="footer">
            
              
              
            
          
            Contact sales
          
          </a>
          
          
        </li>
        
      </ul>
    </li>
    
    <li class="devsite-footer-linkbox ">
    <h3 class="devsite-footer-linkbox-heading no-link">Support</h3>
      <ul class="devsite-footer-linkbox-list">
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//discuss.google.dev/c/google-cloud/14/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 1)"
            target="_blank"track-metadata-position="footer"track-metadata-eventDetail="www.googlecloudcommunity.com"rel="noopener"track-name="google cloud community"track-type="footer link"track-metadata-child_headline="engage"track-metadata-module="footer">
            
          
            Community forums
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/support-hub/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            track-metadata-child_headline="resources"track-metadata-module="footer"track-type="footer link"track-name="support"track-metadata-eventDetail="cloud.google.com/support-hub/"track-metadata-position="footer">
            
          
            Support
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//docs.cloud.google.com/release-notes"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            track-name="release notes"track-metadata-eventDetail="cloud.google.com/release-notes/"track-metadata-child_headline="resources"track-metadata-module="footer"track-type="footer link"track-metadata-position="footer">
            
          
            Release Notes
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//status.cloud.google.com"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            target="_blank"track-metadata-position="footer"track-name="system status"track-metadata-eventDetail="status.cloud.google.com"track-metadata-child_headline="resources"track-metadata-module="footer"track-type="footer link">
            
              
              
            
          
            System status
          
          </a>
          
          
        </li>
        
      </ul>
    </li>
    
    <li class="devsite-footer-linkbox ">
    <h3 class="devsite-footer-linkbox-heading no-link">Resources</h3>
      <ul class="devsite-footer-linkbox-list">
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//github.com/googlecloudPlatform/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 1)"
            track-metadata-position="footer"track-metadata-child_headline="resources"track-metadata-module="footer"track-type="footer link"track-name="github"track-metadata-eventDetail="github.com/googlecloudPlatform/">
            
          
            GitHub
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/docs/get-started/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            track-metadata-child_headline="resources"track-metadata-module="footer"track-type="footer link"track-name="google cloud quickstarts"track-metadata-eventDetail="cloud.google.com/docs/get-started/"track-metadata-position="footer">
            
          
            Getting Started with Google Cloud
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/docs/samples"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            track-metadata-child_headline="resources"track-metadata-module="footer"track-type="footer link"track-name="code samples"track-metadata-eventDetail="cloud.google.com/docs/samples"track-metadata-position="footer">
            
          
            Code samples
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/architecture/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            track-metadata-position="footer"track-metadata-module="footer"track-metadata-child_headline="resources"track-type="footer link"track-name="cloud architecture center"track-metadata-eventDetail="cloud.google.com/architecture/">
            
          
            Cloud Architecture Center
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/learn/training/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 5)"
            track-metadata-position="footer"track-name="training"track-metadata-eventDetail="cloud.google.com/learn/training/"track-metadata-child_headline="resources"track-metadata-module="footer"track-type="footer link">
            
              
              
            
          
            Training and Certification
          
          </a>
          
          
        </li>
        
      </ul>
    </li>
    
    <li class="devsite-footer-linkbox ">
    <h3 class="devsite-footer-linkbox-heading no-link">Engage</h3>
      <ul class="devsite-footer-linkbox-list">
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/blog/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 1)"
            track-name="blog"track-metadata-eventDetail="cloud.google.com/blog/"track-metadata-child_headline="engage"track-metadata-module="footer"track-type="footer link"track-metadata-position="footer">
            
          
            Blog
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/events/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            track-metadata-child_headline="engage"track-metadata-module="footer"track-type="footer link"track-name="events"track-metadata-eventDetail="cloud.google.com/events/"track-metadata-position="footer">
            
          
            Events
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//x.com/googlecloud"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            target="_blank"track-metadata-position="footer"track-name="follow on x"rel="noopener"track-metadata-eventDetail="x.com/googlecloud"track-metadata-child_headline="engage"track-metadata-module="footer"track-type="footer link">
            
          
            X (Twitter)
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//www.youtube.com/googlecloud"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            track-metadata-position="footer"target="_blank"track-type="footer link"track-metadata-child_headline="engage"track-metadata-module="footer"rel="noopener"track-metadata-eventDetail="www.youtube.com/googlecloud"track-name="google cloud on youtube">
            
          
            Google Cloud on YouTube
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//www.youtube.com/googlecloudplatform"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 5)"
            track-metadata-position="footer"target="_blank"track-type="footer link"track-metadata-module="footer"track-metadata-child_headline="engage"track-metadata-eventDetail="www.youtube.com/googlecloudplatform"rel="noopener"track-name="google cloud tech on youtube">
            
              
              
            
          
            Google Cloud Tech on YouTube
          
          </a>
          
          
        </li>
        
      </ul>
    </li>
    
  </ul>
  
</nav>
          
        </devsite-footer-linkboxes>
        <devsite-footer-utility class="devsite-footer">
          
            

<div class="devsite-footer-utility nocontent" data-nosnippet>
  

  
  <nav class="devsite-footer-utility-links" aria-label="Utility links">
    
    <ul class="devsite-footer-utility-list">
      
      <li class="devsite-footer-utility-item
                 ">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="//about.google/"
           data-category="Site-Wide Custom Events"
           data-label="Footer About Google link"
         
           track-metadata-eventDetail="//about.google/"
         
           track-name="about google"
         
           track-type="footer link"
         
           track-metadata-module="utility footer"
         
           target="_blank"
         
           track-metadata-position="footer"
         >
          About Google
        </a>
        
      </li>
      
      <li class="devsite-footer-utility-item
                 devsite-footer-privacy-link">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="//policies.google.com/privacy"
           data-category="Site-Wide Custom Events"
           data-label="Footer Privacy link"
         
           target="_blank"
         
           track-metadata-position="footer"
         
           track-metadata-eventDetail="//policies.google.com/privacy"
         
           track-name="privacy"
         
           track-type="footer link"
         
           track-metadata-module="utility footer"
         >
          Privacy
        </a>
        
      </li>
      
      <li class="devsite-footer-utility-item
                 ">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="//policies.google.com/terms?hl=en"
           data-category="Site-Wide Custom Events"
           data-label="Footer Site terms link"
         
           track-metadata-position="footer"
         
           target="_blank"
         
           track-type="footer link"
         
           track-metadata-module="utility footer"
         
           track-metadata-eventDetail="//www.google.com/intl/en/policies/terms/regional.html"
         
           track-name="site terms"
         >
          Site terms
        </a>
        
      </li>
      
      <li class="devsite-footer-utility-item
                 ">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="//cloud.google.com/product-terms"
           data-category="Site-Wide Custom Events"
           data-label="Footer Google Cloud terms link"
         
           track-metadata-position="footer"
         
           track-metadata-eventDetail="//cloud.google.com/product-terms"
         
           track-name="google cloud terms"
         
           track-type="footer link"
         
           track-metadata-module="utility footer"
         >
          Google Cloud terms
        </a>
        
      </li>
      
      <li class="devsite-footer-utility-item
                 glue-cookie-notification-bar-control">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="#"
           data-category="Site-Wide Custom Events"
           data-label="Footer Manage cookies link"
         
           track-metadata-eventDetail="#"
         
           track-name="Manage cookies"
         
           track-type="footer link"
         
           track-metadata-module="utility footer"
         
           aria-hidden="true"
         
           track-metadata-position="footer"
         >
          Manage cookies
        </a>
        
      </li>
      
      <li class="devsite-footer-utility-item
                 devsite-footer-carbon-button">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="//cloud.google.com/sustainability"
           data-category="Site-Wide Custom Events"
           data-label="Footer Our third decade of climate action: join us link"
         
           track-type="footer link"
         
           track-metadata-module="utility footer"
         
           track-metadata-eventDetail="/sustainability/"
         
           track-name="Our third decade of climate action: join us"
         
           track-metadata-position="footer"
         >
          Our third decade of climate action: join us
        </a>
        
      </li>
      
      <li class="devsite-footer-utility-item
                 devsite-footer-utility-button">
        
        <span class="devsite-footer-utility-description">Sign up for the Google Cloud newsletter</span>
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="//cloud.google.com/newsletter/"
           data-category="Site-Wide Custom Events"
           data-label="Footer Subscribe link"
         
           track-metadata-position="footer"
         
           track-metadata-eventDetail="/newsletter/"
         
           track-name="subscribe"
         
           track-type="footer link"
         
           track-metadata-module="utility footer"
         >
          Subscribe
        </a>
        
      </li>
      
    </ul>
    
    
<devsite-language-selector>
  <ul role="presentation">
    
    
    <li role="presentation">
      <a role="menuitem" lang="en"
        >English</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="de"
        >Deutsch</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="es_419"
        >Español – América Latina</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="fr"
        >Français</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="pt_br"
        >Português – Brasil</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="zh_cn"
        >中文 – 简体</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ja"
        >日本語</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ko"
        >한국어</a>
    </li>
    
  </ul>
</devsite-language-selector>

  </nav>
</div>
          
        </devsite-footer-utility>
        <devsite-panel>
          
        </devsite-panel>
        
      </section>
      </section>
    <devsite-sitemask></devsite-sitemask>
    <devsite-snackbar></devsite-snackbar>
    <devsite-tooltip ></devsite-tooltip>
    <devsite-heading-link></devsite-heading-link>
    <devsite-analytics>
      
        <script type="application/json" analytics>[]</script>
<script type="application/json" tag-management>{&#34;at&#34;: &#34;True&#34;, &#34;ga4&#34;: [], &#34;ga4p&#34;: [], &#34;gtm&#34;: [{&#34;id&#34;: &#34;GTM-5CVQBG&#3100 74622  100 74622    0     0  68343      0  0:00:01  0:00:01 --:--:-- 2068k
4;, &#34;purpose&#34;: 1}], &#34;parameters&#34;: {&#34;internalUser&#34;: &#34;False&#34;, &#34;language&#34;: {&#34;machineTranslated&#34;: &#34;False&#34;, &#34;requested&#34;: &#34;en&#34;, &#34;served&#34;: &#34;en&#34;}, &#34;pageType&#34;: &#34;error&#34;, &#34;projectName&#34;: &#34;Google Cloud Documentation&#34;, &#34;signedIn&#34;: &#34;False&#34;, &#34;tenant&#34;: &#34;clouddocs&#34;, &#34;recommendations&#34;: {&#34;sourcePage&#34;: &#34;&#34;, &#34;sourceType&#34;: 0, &#34;sourceRank&#34;: 0, &#34;sourceIdenticalDescriptions&#34;: 0, &#34;sourceTitleWords&#34;: 0, &#34;sourceDescriptionWords&#34;: 0, &#34;experiment&#34;: &#34;&#34;}, &#34;experiment&#34;: {&#34;ids&#34;: &#34;&#34;}}}</script>
      
    </devsite-analytics>
    
      <devsite-badger></devsite-badger>
    
    
    <cloudx-user></cloudx-user>



  <cloudx-free-trial-eligible-store freeTrialEligible="true"></cloudx-free-trial-eligible-store>

    
<script nonce="eHH6th1yw9H/lubXPP6rJYXb1rvLIH">
  
  (function(d,e,v,s,i,t,E){d['GoogleDevelopersObject']=i;
    t=e.createElement(v);t.async=1;t.src=s;E=e.getElementsByTagName(v)[0];
    E.parentNode.insertBefore(t,E);})(window, document, 'script',
    'https://www.gstatic.com/devrel-devsite/prod/v1b953b434e2033f0160fd97c99360ee5d4d0a613449c2a694360a72d378b9d8e/clouddocs/js/app_loader.js', '[39,"en",null,"/js/devsite_app_module.js","https://www.gstatic.com/devrel-devsite/prod/v1b953b434e2033f0160fd97c99360ee5d4d0a613449c2a694360a72d378b9d8e","https://www.gstatic.com/devrel-devsite/prod/v1b953b434e2033f0160fd97c99360ee5d4d0a613449c2a694360a72d378b9d8e/clouddocs","https://clouddocs-dot-devsite-v2-prod.appspot.com",null,null,["/_pwa/clouddocs/manifest.json","https://www.gstatic.com/devrel-devsite/prod/v1b953b434e2033f0160fd97c99360ee5d4d0a613449c2a694360a72d378b9d8e/images/video-placeholder.svg","https://www.gstatic.com/devrel-devsite/prod/v1b953b434e2033f0160fd97c99360ee5d4d0a613449c2a694360a72d378b9d8e/clouddocs/images/favicons/onecloud/favicon.ico","https://www.gstatic.com/devrel-devsite/prod/v1b953b434e2033f0160fd97c99360ee5d4d0a613449c2a694360a72d378b9d8e/clouddocs/images/lockup.svg","https://fonts.googleapis.com/css?family=Google+Sans:400,500|Roboto:400,400italic,500,500italic,700,700italic|Roboto+Mono:400,500,700&display=swap"],1,null,[1,6,8,12,14,17,21,25,50,52,63,70,75,76,80,87,91,92,93,97,98,100,101,102,103,104,105,107,108,109,110,112,113,117,118,120,122,124,125,126,127,129,130,131,132,133,134,135,136,138,140,141,147,148,149,151,152,156,157,158,159,161,163,164,168,169,170,179,180,182,183,186,191,193,196],"AIzaSy...EEI8","AIzaSy...P0hg","docs.cloud.google.com","AIzaSy...6J4o","AIzaSy...70KY",null,null,null,["OnSwitch__enable","Cloud__enable_llm_concierge_chat","Profiles__enable_callout_notifications","MiscFeatureFlags__enable_variable_operator_index_yaml","DevPro__enable_g1_integration","Search__enable_page_map","Cloud__enable_legacy_calculator_redirect","Cloud__enable_cloud_dlp_service","DevPro__enable_embed_profile_creation","TpcFeatures__enable_unmirrored_page_left_nav","Profiles__enable_completequiz_endpoint","Profiles__enable_purchase_prompts","MiscFeatureFlags__fix_lower_breadcrumbs","MiscFeatureFlags__enable_variable_operator","CloudShell__cloud_code_overflow_menu","Profiles__enable_playlist_community_acl","Analytics__enable_devpro_interaction_logging","DevPro__enable_devpro_offers","Profiles__enable_user_type","Profiles__enable_developer_profile_pages_as_content","Profiles__enable_page_saving","MiscFeatureFlags__gdp_dashboard_reskin_enabled","DevPro__enable_google_payments_buyflow","Concierge__enable_pushui","MiscFeatureFlags__developers_footer_dark_image","MiscFeatureFlags__enable_dark_theme","MiscFeatureFlags__enable_explain_this_code","DevPro__enable_cloud_innovators_plus","DevPro__enable_developer_subscriptions","Cloud__enable_cloud_shell","MiscFeatureFlags__enable_firebase_utm","Concierge__enable_devsite_llm_tools","MiscFeatureFlags__developers_footer_image","SignIn__enable_l1_signup_flow","DevPro__enable_vertex_credit_card","Search__enable_dynamic_content_confidential_banner","Cloud__cache_serialized_dynamic_content","Concierge__enable_remove_info_panel_tags","DevPro__remove_eu_tax_intake_form","Cloud__enable_cloud_shell_fte_user_flow","DevPro__enable_firebase_workspaces_card","Profiles__enable_stripe_subscription_management","Search__enable_ai_eligibility_checks","Profiles__enable_profile_collections","Experiments__reqs_query_experiments","MiscFeatureFlags__enable_appearance_cookies","Profiles__enable_targeted_hero","Profiles__enable_public_developer_profiles","Concierge__enable_concierge_restricted","Cloud__fast_free_trial","Profiles__enable_developer_profile_benefits_ui_redesign","MiscFeatureFlags__enable_explicit_template_dependencies","Profiles__enable_auto_apply_credits","CloudShell__cloud_shell_button","Profiles__enable_complete_playlist_endpoint","Profiles__enable_dashboard_curated_recommendations","Cloud__enable_cloudx_experiment_ids","DevPro__enable_devsite_captcha","Concierge__enable_actions_menu","Profiles__enable_join_program_group_endpoint","Search__enable_suggestions_from_borg","Search__enable_ai_search_summaries_for_all","DevPro__enable_code_assist","DevPro__enable_credits_banner","BookNav__enable_tenant_cache_key","Analytics__enable_clearcut_logging","MiscFeatureFlags__enable_view_transitions","Cloud__enable_free_trial_server_call","MiscFeatureFlags__enable_project_variables","Profiles__enable_developer_profiles_callout","TpcFeatures__proxy_prod_host","DevPro__enable_nvidia_credits_card","MiscFeatureFlags__enable_framebox_badge_methods","Profiles__enable_completecodelab_endpoint","Profiles__require_profile_eligibility_for_signin","Profiles__enable_recognition_badges","MiscFeatureFlags__remove_cross_domain_tracking_params","DevPro__enable_enterprise","EngEduTelemetry__enable_engedu_telemetry","DevPro__enable_free_benefits","DevPro__enable_google_one_card","Profiles__enable_awarding_url"],null,null,"AIzaSy...kCVE","https://developerscontentserving-pa.clients6.google.com","AIzaSy...lO-k","https://developerscontentsearch-pa.clients6.google.com",1,4,1,"https://developerprofiles-pa.clients6.google.com",[39,"clouddocs","Google Cloud Documentation","docs.cloud.google.com",null,"clouddocs-dot-devsite-v2-prod.appspot.com",null,null,[1,1,null,null,null,null,null,null,null,null,null,[1],null,null,null,null,null,1,[1],[null,null,null,[1,20],"/terms/recommendations"],[1],null,[1],[1,null,1],null,[1]],null,[54,null,null,null,null,null,"/images/lockup.svg","/images/favicons/onecloud/apple-icon.png",null,null,null,1,1,1,1,null,[],null,null,[[],[],[],[],[],[],[],[]],null,1,null,null,null,"/images/lockup-dark-theme.svg",[]],[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[6,1,14,15,22,23,29,37],null,[[null,null,null,null,null,null,[1,[["docType","Choose a content type",[["ApiReference",null,null,null,null,null,null,null,null,"API reference"],["Sample",null,null,null,null,null,null,null,null,"Code sample"],["ReferenceArchitecture",null,null,null,null,null,null,null,null,"Reference architecture"],["Tutorial",null,null,null,null,null,null,null,null,"Tutorial"]]],["category","Choose a topic",[["AiAndMachineLearning",null,null,null,null,null,null,null,null,"Artificial intelligence and machine learning (AI/ML)"],["ApplicationDevelopment",null,null,null,null,null,null,null,null,"Application development"],["BigDataAndAnalytics",null,null,null,null,null,null,null,null,"Big data and analytics"],["Compute",null,null,null,null,null,null,null,null,"Compute"],["Containers",null,null,null,null,null,null,null,null,"Containers"],["Databases",null,null,null,null,null,null,null,null,"Databases"],["HybridCloud",null,null,null,null,null,null,null,null,"Hybrid and multicloud"],["LoggingAndMonitoring",null,null,null,null,null,null,null,null,"Logging and monitoring"],["Migrations",null,null,null,null,null,null,null,null,"Migrations"],["Networking",null,null,null,null,null,null,null,null,"Networking"],["SecurityAndCompliance",null,null,null,null,null,null,null,null,"Security and compliance"],["Serverless",null,null,null,null,null,null,null,null,"Serverless"],["Storage",null,null,null,null,null,null,null,null,"Storage"]]]]]],[1],null,1],[[null,null,null,null,null,["GTM-5CVQBG"],null,null,null,null,null,[["GTM-5CVQBG",2]],1],null,null,null,null,null,1],"mwETRvWii0eU5NUYprb0Y9z5GVbc",4],null,"pk_live_5170syrHvgGVmSx9sBrnWtA5luvk9BwnVcvIi7HizpwauFG96WedXsuXh790rtij9AmGllqPtMLfhe2RSwD6Pn38V00uBCydV4m",1,null,"https://developerscontentinsights-pa.clients6.google.com","AIzaSy...SBDU","AIzaSy...MRsE","https://developers.clients6.google.com",null,null,"AIzaSy...7PmI\n",null,null,"https://developers.googleapis.com"]')
  
</script>

    <devsite-a11y-announce></devsite-a11y-announce>
  </body>
</html>