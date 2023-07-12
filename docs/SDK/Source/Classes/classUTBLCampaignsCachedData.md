---
title: UTBLCampaignsCachedData
type: class
aliases: UTBLCampaignsCachedData
share: false

---

# UTBLCampaignsCachedData





Inherits from UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[[GetCachedCampaignComplete]]**(const [FCampaignCacheData](/docs/SDK/Source/Classes/structFCampaignCacheData.md) & CachedData, TScriptInterface< [ICampaign](/docs/SDK/Source/Classes/classICampaign.md) > Campaign) |
| float | **[[GetCachedCampaignDataProgress]]**(const [FCampaignCacheData](/docs/SDK/Source/Classes/structFCampaignCacheData.md) & CachedData, TScriptInterface< [ICampaign](/docs/SDK/Source/Classes/classICampaign.md) > Campaign) |
| bool | **[[GetCachedData]]**(TScriptInterface< [ICampaign](/docs/SDK/Source/Classes/classICampaign.md) > InCampaign, [FCampaignCacheData](/docs/SDK/Source/Classes/structFCampaignCacheData.md) & OutData) const |
| bool | **[[HasSameData]]**(const [FCampaignCacheData](/docs/SDK/Source/Classes/structFCampaignCacheData.md) & CachedData, TScriptInterface< [ICampaign](/docs/SDK/Source/Classes/classICampaign.md) > Campaign) |
| void | **[[InitFromActiveCampaigns]]**([UCampaignList](/docs/SDK/Source/Classes/classUCampaignList.md) * InCampaignList) |
| | **[[UTBLCampaignsCachedData]]**() |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200