## V0.1 - 5/12/2023
### added
- Started testing with the dialogue to relationship system. got basic concept down.
- image system developed

## VO.1.1 - 5/14/2023
### added
- added basic action menu
- added movement function (both are still very WIP)
- added early relationship level code

## V0.2 - 5/30/2023

### Added
Added movement/location menu
Adding characters to interact with
Added conversation feature to Lana (will be reused for other characters)
Added intro for Lana (will be reused for other characters
Added basic “attend class” feature
Added relationship levels going up depending on dialogue choice
Added limited day time feature (you can only do so much in one day before the next day happens, still WIP)
Added option to check relationship levels with each character

### Changed
Overhauled conversation system
Renamed testmap.py to map.py
Renamed changelog.py to checklist.py, now has list of things needed for alpha/beta versions

### Removed
Image system was removed because code wouldn’t work with it, and it was too big to add within time limit
Removed test.py
Removed functions.py
Removed visual.py
Removed images folder

## V0.2.1 - 5/31/2023

### Added
Added conversations to Lana and Sid
Added day system (still WIP)
Added end ranking system (still WIP)
Added textwrap import to have text indent properly in console/gameplay
Added intros.py

### Changed
Redid intro system to be simpler to squash bugs
Edited some lines to be under 79 characters (dialogue strings)

### Fixed
Fixed some text strings not indenting correctly with textwrap import

## V0.3 (Alpha) - 6/3/2023

### Added
Added intro to Stephen and Sid
Added conversations to Connor and Stephen
Added menu for movement, hints, relationships and quitting
Added classes.py
Added messages when relationship is maxed out
Added different text when you interact with a character without yet meeting them

### Changed
Unlocked dialogue options can no longer be used multiple times
Attend class functions moved to classes.py

### Removed
Removed textwrap since it wasn't needed

### Fixed
Fixed bug in testing where entering Talk wouldn't print out conversation text

## V0.4 (Beta) - 6/3/2023

### Added
Added messages for incorrect inputs
Added different attend class messages for all classes if character is not met

### Changed
Action count per day has been bumped up to 5 (from tester feedback)
Finished end ranking system
Finished day system

### Fixed
Fixed issue where days would go into the negatives
Fixed issue where typing in capital letters in some instances would give an error
Fixed parts of code where Lana was referenced instead of Sid

## V1.0 (Final) - 6/5/2023

### Added
Added header with credits, title, date, etc
Added game description to header
Added comments for code
Added docstrings for code

### Changed
Code is now in PEP8 format

### Fixed
Fixed ending screen not tallying all relationship levels
Fixed typos and misspellings
Fixed issue where player started at 6 actions instead of 5
Fixed some variables being assigned to the wrong characters

## Final Note
Sorry that this is a seperate fork from 0.1 and 0.1.1. Trying to commit
any changes to it wouldn't work, so we made a new fork that would
actually work for it.
- Jake