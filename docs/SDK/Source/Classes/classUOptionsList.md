---
title: UOptionsList
type: class
aliases: UOptionsList
share: false

---

# UOptionsList





Inherits from UWidget

## Public Functions

|                | Name           |
| -------------- | -------------- |
| UWidget * | **[[GetSelectedWidget]]**() |
| bool | **[[IsFirstEntry]]**(const UObject * Object) const |
| bool | **[[IsFirstEntryInSubcategory]]**(const UObject * Object) const |
| void | **[[SelectWidget]]**(UObject * Item) |
| void | **[[SetCategory]]**([UOptionsScreenCategory](/docs/SDK/Source/Classes/classUOptionsScreenCategory.md) * InCategory) |
| | **[[UOptionsList]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [UOptionsScreenCategory](/docs/SDK/Source/Classes/classUOptionsScreenCategory.md) * | **[[Category]]**  |
| float | **[[ItemHeight]]**  |
| TArray< UObject * > | **[[Items]]**  |
| FOnGenerateCheckbox | **[[OnGenerateCheckboxEvent]]**  |
| FOnGenerateComboBox | **[[OnGenerateComboBoxEvent]]**  |
| FOnGenerateKeybind | **[[OnGenerateKeybindEvent]]**  |
| FOnGenerateSlider | **[[OnGenerateSliderEvent]]**  |
| FOnGenerateSubcategoryHeader | **[[OnGenerateSubcategoryHeaderEvent]]**  |
| FOnItemSelected | **[[OnItemSelected]]**  |
| FName | **[[TableRowStyleName]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [UTBLScrollBarStyleDataAsset](/docs/SDK/Source/Classes/classUTBLScrollBarStyleDataAsset.md) * | **[[ScrollBarStyle]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200