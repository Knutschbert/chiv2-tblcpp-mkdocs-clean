---
title: ICampaignPurchasable
type: class
aliases: ICampaignPurchasable
share: false

---

# ICampaignPurchasable





Inherits from IInterface

Inherited by [UCampaignImpl](/docs/SDK/Source/Classes/classUCampaignImpl.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual void | **[[BindOnPurchasedChanged]]**(const FOnCampaignPurchasedChanged & Delegate) |
| virtual FString | **[[GetStoreOfferId]]**() const |
| virtual [FStoreOfferItem](/docs/SDK/Source/Classes/structFStoreOfferItem.md) | **[[GetStoreOfferItem]]**() const |
| virtual void virtual void virtual bool | **[[IsPurchased]]**() const |
| virtual void virtual void | **[[SetPurchased]]**() |
| FString return | **[[TEXT]]**("" ) |
| virtual void | **[[UnbindOnPurchasedChanged]]**(const FOnCampaignPurchasedChanged & Delegate) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [FStoreOfferItem](/docs/SDK/Source/Classes/structFStoreOfferItem.md) return | **[[FStoreOfferItem]]**  |
| void virtual void virtual bool return | **[[false]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200