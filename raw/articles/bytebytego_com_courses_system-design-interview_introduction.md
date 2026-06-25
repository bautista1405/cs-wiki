---
original_url: https://bytebytego.com/courses/system-design-interview/introduction
fetched: 2026-05-08
source_tool: curl
---

% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0<!DOCTYPE html><html data-dpl-id="dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c"><head><meta charSet="utf-8" data-next-head=""/><title data-next-head="">ByteByteGo | Technical Interview Prep</title><meta name="robots" content="index,follow" data-next-head=""/><meta name="description" content="Everything you need to take your system design skill to the next level" data-next-head=""/><meta name="twitter:card" content="summary_large_image" data-next-head=""/><meta name="twitter:site" content="@bytebytego" data-next-head=""/><meta name="twitter:creator" content="@bytebytego" data-next-head=""/><meta property="og:title" content="System Design · Coding · Behavioral · Machine Learning Interviews" data-next-head=""/><meta property="og:description" content="Ace Every Stage of Your Next Technical Interview" data-next-head=""/><meta property="og:url" content="https://bytebytego.com" data-next-head=""/><meta property="og:type" content="website" data-next-head=""/><meta property="og:image" content="https://bytebytego.com/social2.png" data-next-head=""/><meta property="og:image:alt" content="ByteByteGo Logo" data-next-head=""/><meta property="og:image:type" content="image/png" data-next-head=""/><meta property="og:image:width" content="2400" data-next-head=""/><meta property="og:image:height" content="1260" data-next-head=""/><meta property="og:locale" content="en_US" data-next-head=""/><meta property="og:site_name" content="ByteByteGo" data-next-head=""/><link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" data-next-head=""/><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png" data-next-head=""/><link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png" data-next-head=""/><link rel="manifest" href="/site.webmanifest" data-next-head=""/><link rel="mask-icon" href="/safari-pinned-tab.svg" color="#5bbad5" data-next-head=""/><meta name="msapplication-TileColor" content="#da532c" data-next-head=""/><meta name="theme-color" content="#ffffff" data-next-head=""/><meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1,user-scalable=0" data-next-head=""/><meta name="format-detection" content="telephone=no, date=no, email=no, address=no" data-next-head=""/><style id="ios-text-size-adjust" data-next-head="">
  html,
  body {
    -webkit-text-size-adjust: 100%;
    text-size-adjust: 100%;
  }
</style><link rel="preload" href="/_next/static/media/logo.13avpmsgkn3l3.svg?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" as="image" data-next-head=""/><script id="bytebytego-announcement-banner-bootstrap">
(function () {
  try {
    if (window.localStorage.getItem('HIDE_AI_COHORT3_BANNER')) {
      document.documentElement.dataset.bytebytegoAnnouncementBannerHidden = 'true';
      document.documentElement.style.setProperty('--bytebytego-announcement-banner-display', 'none');
      document.documentElement.style.setProperty('--bytebytego-announcement-banner-offset', '0px');
    }
  } catch (error) {}
})();
</script><script id="bytebytego-consent-bootstrap">
(function () {
  var consentEnabled = true;
  var categories = ['necessary', 'functional', 'analytics', 'performance', 'advertisement'];

  var categoryState = consentEnabled
    ? {
        necessary: true,
        functional: false,
        analytics: false,
        performance: false,
        advertisement: false,
      }
    : {
        necessary: true,
        functional: true,
        analytics: true,
        performance: true,
        advertisement: true,
      };

  var activeLaw = null;
  var consentReady = !consentEnabled;
  var listeners = new Set();

  var readCookieValue = function (cookieString, name) {
    var cookiePrefix = name + '=';
    var entries = cookieString.split(';');

    for (var index = 0; index < entries.length; index += 1) {
      var entry = entries[index] ? entries[index].trim() : '';
      if (!entry || entry.indexOf(cookiePrefix) !== 0) {
        continue;
      }

      try {
        return decodeURIComponent(entry.slice(cookiePrefix.length));
      } catch (_error) {
        return '';
      }
    }

    return '';
  };

  var parseCookieCategories = function (cookieValue) {
    if (!cookieValue) {
      return null;
    }

    var nextState = Object.assign({}, categoryState);
    var sawCategory = false;
    var entries = cookieValue.split(',');

    for (var index = 0; index < entries.length; index += 1) {
      var parts = entries[index].split(':');
      var rawKey = parts[0];
      var rawValue = parts[1];

      if (!rawKey || !rawValue) {
        continue;
      }

      var key = rawKey.trim().toLowerCase();
      var value = rawValue.trim().toLowerCase();

      if (categories.indexOf(key) === -1) {
        continue;
      }

      nextState[key] = value === 'yes' || value === 'true';
      sawCategory = true;
    }

    return sawCategory ? nextState : null;
  };

  var normalizeCategoryState = function (input) {
    if (!input || typeof input !== 'object') {
      return null;
    }

    var normalized = Object.assign({}, categoryState);
    var sawCategory = false;

    for (var index = 0; index < categories.length; index += 1) {
      var key = categories[index];
      if (typeof input[key] !== 'boolean') {
        continue;
      }

      normalized[key] = input[key];
      sawCategory = true;
    }

    return sawCategory ? normalized : null;
  };

  var emitChange = function () {
    var detail = {
      enabled: consentEnabled,
      ready: consentReady,
      activeLaw: activeLaw,
      categories: Object.assign({}, categoryState),
    };

    window.dispatchEvent(
      new CustomEvent('bytebyte_consent_update', {
        detail: detail,
      })
    );

    listeners.forEach(function (listener) {
      try {
        listener(detail);
      } catch (error) {
        console.warn('[consent] failed to notify a consent listener', error);
      }
    });
  };

  if (consentEnabled) {
    var cookieCategories = parseCookieCategories(
      readCookieValue(document.cookie, 'cookieyes-consent')
    );

    if (cookieCategories) {
      categoryState = cookieCategories;
      consentReady = true;
    }

    document.addEventListener('cookieyes_banner_load', function (event) {
      var detail = event && typeof event === 'object' ? event.detail : undefined;

      var normalizedCategories = normalizeCategoryState(
        detail && detail.categories
      );

      if (normalizedCategories) {
        categoryState = normalizedCategories;
      }

      if (
        detail &&
        typeof detail.activeLaw === 'string' &&
        detail.activeLaw
      ) {
        activeLaw = detail.activeLaw.trim().toLowerCase();
      }

      consentReady = true;
      emitChange();
    });

    document.addEventListener('cookieyes_consent_update', function (event) {
      var detail = event && typeof event === 'object' ? event.detail : undefined;

      if (
        (detail && Array.isArray(detail.accepted)) ||
        (detail && Array.isArray(detail.rejected))
      ) {
        var nextState = Object.assign({}, categoryState);

        if (detail && Array.isArray(detail.accepted)) {
          for (var index = 0; index < detail.accepted.length; index += 1) {
            var acceptedKey = String(detail.accepted[index])
              .trim()
              .toLowerCase();

            if (categories.indexOf(acceptedKey) === -1) {
              continue;
            }

            nextState[acceptedKey] = true;
          }
        }

        if (detail && Array.isArray(detail.rejected)) {
          for (var index = 0; index < detail.rejected.length; index += 1) {
            var rejectedKey = String(detail.rejected[index])
              .trim()
              .toLowerCase();

            if (categories.indexOf(rejectedKey) === -1) {
              continue;
            }

            nextState[rejectedKey] = false;
          }
        }

        nextState.necessary = true;
        categoryState = nextState;
      } else {
        var normalizedCategories = normalizeCategoryState(
          detail && detail.categories
        );

        if (normalizedCategories) {
          categoryState = normalizedCategories;
        }
      }

      consentReady = true;
      emitChange();
    });
  }

  var getCategoryConsentState = function (category) {
    if (!consentEnabled) {
      return 'granted';
    }

    if (!consentReady) {
      return 'unknown';
    }

    var key = String(category).trim().toLowerCase();
    if (categories.indexOf(key) === -1) {
      return 'unknown';
    }

    return categoryState[key] ? 'granted' : 'denied';
  };

  var getAdvertisingStorageConsentState = function () {
    return getCategoryConsentState('advertisement');
  };

  window.bytebyteConsent = {
    isEnabled: consentEnabled,
    isReady: function () {
      return consentReady;
    },
    getActiveLaw: function () {
      return activeLaw;
    },
    getCategories: function () {
      return Object.assign({}, categoryState);
    },
    getCategoryConsentState: getCategoryConsentState,
    getAdvertisingStorageConsentState: getAdvertisingStorageConsentState,
    hasCategoryConsent: function (category) {
      return getCategoryConsentState(category) === 'granted';
    },
    onChange: function (listener) {
      if (typeof listener !== 'function') {
        return function () {};
      }

      listeners.add(listener);
      return function () {
        listeners.delete(listener);
      };
    },
  };

  emitChange();
})();
</script><script id="bytebytego-cookieyes-consent-defaults">window.dataLayer = window.dataLayer || [];function gtag(){dataLayer.push(arguments);}gtag('consent','default',{"ad_storage":"denied","ad_user_data":"denied","ad_personalization":"denied","analytics_storage":"denied","functionality_storage":"granted","personalization_storage":"denied","security_storage":"granted","wait_for_update":2000,"region":["AT","BE","BG","HR","CY","CZ","DK","EE","FI","FR","DE","GR","HU","IS","IE","IT","LV","LI","LT","LU","MT","NL","NO","PL","PT","RO","SK","SI","ES","SE","GB","CH"]});gtag('consent','default',{"ad_storage":"granted","ad_user_data":"granted","ad_personalization":"granted","analytics_storage":"granted","functionality_storage":"granted","personalization_storage":"granted","security_storage":"granted"});gtag('set','ads_data_redaction',true);gtag('set','url_passthrough',true);</script><link rel="preconnect" href="https://firebase.googleapis.com"/><link rel="preconnect" href="https://www.googletagmanager.com"/><link rel="preconnect" href="https://vercel.live"/><link rel="preconnect" href="https://www.googleapis.com"/><link rel="preload" href="/_next/static/chunks/0n~e1vpsyyyy-.css?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" as="style"/><link rel="stylesheet" href="/_next/static/chunks/0n~e1vpsyyyy-.css?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" data-n-g=""/><link rel="preload" href="/_next/static/chunks/0tdzihfr8__~-.css?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" as="style"/><link rel="stylesheet" href="/_next/static/chunks/0tdzihfr8__~-.css?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" data-n-g=""/><link rel="preload" href="/_next/static/chunks/17p376yuc06jb.css?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" as="style"/><link rel="stylesheet" href="/_next/static/chunks/17p376yuc06jb.css?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" data-n-p=""/><noscript data-n-css=""></noscript><script src="/_next/static/chunks/14nhe6jhxmtqn.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/chunks/0r-1q2ccohcx5.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/chunks/04.h0hq_yz021.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/chunks/0e01ekw4e0vyl.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/chunks/0ybcip2ey3f8q.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/chunks/0ntx5j~gvqakq.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/chunks/067159ebye~my.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/chunks/00q4k7gh_.z~n.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/chunks/0eg~mcich8d~n.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/chunks/0a7wp00g651j3.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/chunks/0an9vhfme25um.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/chunks/09x2.~y4g0cul.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/chunks/15qv70zcgrqx6.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/chunks/17mgwoa_o4ubw.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/chunks/15yjsiwikxuxm.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/chunks/124qifhnhpu2r.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/chunks/0noxqutw2gpj~.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/chunks/10jr5xyoaz-jo.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/chunks/0ah-~9tqao1.r.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/chunks/12h9~ezq3t.m8.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/chunks/12mnskwraalvv.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/chunks/010~466iv.q14.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/chunks/0wwze_~kuwdt2.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/chunks/turbopack-0usedwlzioqwh.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/chunks/16deug9fc70n8.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/chunks/turbopack-0a_378c96nd~q.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/build-TfctsWXpff2fKS/_buildManifest.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/build-TfctsWXpff2fKS/_ssgManifest.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script><script src="/_next/static/build-TfctsWXpff2fKS/_clientMiddlewareManifest.js?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c" defer=""></script></head><body><div id="__next"><div class="ant-layout css-133v4sd"><header class="ant-layout-header style-module-scss-module__nG5F8W__header style-module-scss-module__nG5F8W__light css-133v4sd" style="border-width:1px;top:0px"><a class="style-module-scss-module__nG5F8W__headerLogoLink" href="/"><img alt="ByteByteGo logo" decoding="async" data-nimg="fill" class="style-module-scss-module__nG5F8W__headerLogoImage" style="position:absolute;height:100%;width:100%;left:0;top:0;right:0;bottom:0;color:transparent" src="/_next/static/media/logo.13avpmsgkn3l3.svg?dpl=dpl_CEjisbLnWxFQGUTRjiHGoKY1oV5c"/></a><div class="style-module-scss-module__nG5F8W__headerRight"><div class="style-module-scss-module__nG5F8W__navLinkSlot style-module-scss-module__nG5F8W__navLinkSlotHiddenOnMobile"><span class="style-module-scss-module__nG5F8W__navLinkPlaceholder" aria-hidden="true"></span></div><div class="style-module-scss-module__nG5F8W__headerProfileWrap"><div class="style-module-scss-module__nG5F8W__accountSlot style-module-scss-module__nG5F8W__accountSlotReserved"><div class="style-module-scss-module__nG5F8W__accountPlaceholder" aria-hidden="true"></div></div></div></div></header><main class="ant-layout-content css-133v4sd" style="margin-top:var(--bytebytego-header-height, 64px)"><div class="_error-module-scss-module__fcLJlG__errorPage" role="alert" aria-live="assertive"><div class="_error-module-scss-module__fcLJlG__errorContainer"><h1 class="_error-module-scss-module__fcLJlG__errorCode" aria-label="Error 404">404</h1><h2 id="error-page-title" class="_error-module-scss-module__fcLJlG__errorTitle">Page Not Found</h2><p class="_error-module-scss-module__fcLJlG__errorMessage" aria-describedby="error-page-title">The page you&#x27;re looking for doesn&#x27;t exist.</p><div class="_error-module-scss-module__fcLJlG__errorActions"><button class="_e
100 16775    0 16775    0     0  63077      0 --:--:-- --:--:-- --:--:-- 63301
rror-module-scss-module__fcLJlG__btnPrimary" aria-label="Navigate to the homepage">Go to Homepage</button></div></div></div></main></div><!--$--><!--/$--></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{}},"page":"/404","query":{},"buildId":"build-TfctsWXpff2fKS","nextExport":true,"autoExport":true,"isFallback":false,"scriptLoader":[]}</script></body></html>