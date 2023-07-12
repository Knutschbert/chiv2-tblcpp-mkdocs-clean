---
title: UOptionsDropDownList
type: class
aliases: UOptionsDropDownList
share: false

---

# UOptionsDropDownList





Inherits from UWidget

## Public Functions

|                | Name           |
| -------------- | -------------- |
| int32 | **[[AddItem]]**(FText Text, int32 Index) |
| UWidget * | **[[GetSelectedWidget]]**() |
| void | **[[RemoveAllItems]]**() |
| void | **[[SetItemSelection]]**(UPARAM(Ref) [UDropDownListItem](/docs/SDK/Source/Classes/classUDropDownListItem.md) *& InItem, bool bSelected, TEnumAsByte< ESelectInfo::Type > Type) |
| | **[[UOptionsDropDownList]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[ItemHeight]]**  |
| TArray< [UDropDownListItem](/docs/SDK/Source/Classes/classUDropDownListItem.md) * > | **[[Items]]**  |
| FOnGenerateEntry | **[[OnGenerateRowEvent]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200