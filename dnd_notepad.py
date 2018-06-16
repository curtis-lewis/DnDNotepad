from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from MainWindow import Ui_MainWindow
from random import *
import sys
import json

# pyuic5 -x alpha_ui.ui -o MainWindow.py

class ApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # filename initialization
        self.filename = ''

        # character dictionary initialization
        self.character = {
         'character_name': '',
         'class': '',
         'background': '',
         'player_name': '',
         'race': '',
         'alignment': '',
         'experience_points': '',
         'strength': 0,
         'dexterity': 0,
         'constitution': 0,
         'intelligence': 0,
         'wisdom': 0,
         'charisma': 0,
         'armor_class': '',
         'initiative': '',
         'speed': '',
         'current_hp': '',
         'total_hit_dice':'',
         'hit_dice': '',
         'str_saving_throw': False,
         'dex_saving_throw': False,
         'con_saving_throw': False,
         'int_saving_throw': False,
         'wis_saving_throw': False,
         'cha_saving_throw': False,
         'acrobatics': False,
         'animal_handling': False,
         'arcana': False,
         'athletics': False,
         'deception': False,
         'history': False,
         'insight': False,
         'intimidation': False,
         'investigation': False,
         'medicine': False,
         'nature': False,
         'perception': False,
         'performance': False,
         'persuassion': False,
         'religion': False,
         'sleight_of_hand': False,
         'stealth': False,
         'survival': False,
         'success_ds1': False,
         'success_ds2': False,
         'success_ds3': False,
         'failure_ds1': False,
         'failure_ds2': False,
         'failure_ds3': False,
         'personality_traits': '',
         'ideals': '',
         'bonds': '',
         'flaws': '',
         'features': '',
         'weapon1_name': '',
         'weapon1_attack': 0,
         'weapon1_type': '',
         'weapon2_name': '',
         'weapon2_attack': 0,
         'weapon2_type': '',
         'weapon3_name': '',
         'weapon3_attack': 0,
         'weapon3_type': '',
         'weapon4_name': '',
         'weapon4_attack': 0,
         'weapon4_type': '',
         'weapon_info': '',
         'languages': '',
         'equipment': '',
         'notes': ''
         }

        self.characterTemplate = {
         'character_name': '',
         'class': '',
         'background': '',
         'player_name': '',
         'race': '',
         'alignment': '',
         'experience_points': '',
         'strength': 0,
         'dexterity': 0,
         'constitution': 0,
         'intelligence': 0,
         'wisdom': 0,
         'charisma': 0,
         'armor_class': '',
         'initiative': '',
         'speed': '',
         'current_hp': '',
         'total_hit_dice':'',
         'hit_dice': '',
         'str_saving_throw': False,
         'dex_saving_throw': False,
         'con_saving_throw': False,
         'int_saving_throw': False,
         'wis_saving_throw': False,
         'cha_saving_throw': False,
         'acrobatics': False,
         'animal_handling': False,
         'arcana': False,
         'athletics': False,
         'deception': False,
         'history': False,
         'insight': False,
         'intimidation': False,
         'investigation': False,
         'medicine': False,
         'nature': False,
         'perception': False,
         'performance': False,
         'persuassion': False,
         'religion': False,
         'sleight_of_hand': False,
         'stealth': False,
         'survival': False,
         'success_ds1': False,
         'success_ds2': False,
         'success_ds3': False,
         'failure_ds1': False,
         'failure_ds2': False,
         'failure_ds3': False,
         'personality_traits': '',
         'ideals': '',
         'bonds': '',
         'flaws': '',
         'features': '',
         'weapon1_name': '',
         'weapon1_attack': 0,
         'weapon1_type': '',
         'weapon2_name': '',
         'weapon2_attack': 0,
         'weapon2_type': '',
         'weapon3_name': '',
         'weapon3_attack': 0,
         'weapon3_type': '',
         'weapon4_name': '',
         'weapon4_attack': 0,
         'weapon4_type': '',
         'weapon_info': '',
         'languages': '',
         'equipment': '',
         'notes': ''
         }
 
        # set default combo box values
        self.character['class'] = self.ui.class_combo.currentText()
        self.character['race'] = self.ui.race_combo.currentText()
        self.character['alignment'] = self.ui.alignment_combo.currentText()
        # ********************************************************

        # set default mod values on start up
        self.showStrModValue()
        self.showDexModValue()
        self.showConModValue()
        self.showIntModValue()
        self.showWisModValue()
        self.showChaModValue()
        
        # Description connect
        self.ui.characterName_le.editingFinished.connect(self.characterNameChange)
        self.ui.class_combo.currentIndexChanged.connect(self.classChange)
        self.ui.background_le.editingFinished.connect(self.backgroundChange)
        self.ui.playerName_le.editingFinished.connect(self.playerNameChange)
        self.ui.race_combo.currentIndexChanged.connect(self.raceChange)
        self.ui.alignment_combo.currentIndexChanged.connect(self.alignmentChange)
        self.ui.xp_le.editingFinished.connect(self.experiencePointsChange)
        self.ui.strengthSavingThrow_cb.stateChanged.connect(self.strSavingThrowChange)
        self.ui.dexteritySavingThrow_cb.stateChanged.connect(self.dexSavingThrowChange)
        self.ui.constitutionSavingThrow_cb.stateChanged.connect(self.conSavingThrowChange)
        self.ui.intelligenceSavingThrow_cb.stateChanged.connect(self.intSavingThrowChange)
        self.ui.wisdomSavingThrow_cb.stateChanged.connect(self.wisSavingThrowChange)
        self.ui.charismaSavingThrow_cb.stateChanged.connect(self.chaSavingThrowChange)
        self.ui.acrobatics_cb.stateChanged.connect(self.acrobaticsChange)
        self.ui.animalHandling_cb.stateChanged.connect(self.animalHandlingChange)
        self.ui.arcana_cb.stateChanged.connect(self.arcanaChange)
        self.ui.athletics_cb.stateChanged.connect(self.athleticsChange)
        self.ui.deception_cb.stateChanged.connect(self.deceptionChange)
        self.ui.history_cb.stateChanged.connect(self.historyChange)
        self.ui.insight_cb.stateChanged.connect(self.insightChange)
        self.ui.intimidation_cb.stateChanged.connect(self.intimidationChange)
        self.ui.investigation_cb.stateChanged.connect(self.investigationChange)
        self.ui.medicine_cb.stateChanged.connect(self.medicineChange)
        self.ui.nature_cb.stateChanged.connect(self.natureChange)
        self.ui.perception_cb.stateChanged.connect(self.perceptionChange)
        self.ui.performance_cb.stateChanged.connect(self.performanceChange)
        self.ui.persuassion_cb.stateChanged.connect(self.persuassionChange)
        self.ui.religion_cb.stateChanged.connect(self.religionChange)
        self.ui.sleightOfHand_cb.stateChanged.connect(self.sleightOfHandChange)
        self.ui.stealth_cb.stateChanged.connect(self.stealthChange)
        self.ui.survival_cb.stateChanged.connect(self.survivalChange)
        self.ui.armorClass_le.editingFinished.connect(self.armorClassChange)
        self.ui.initiative_le.editingFinished.connect(self.initiativeChange)
        self.ui.speed_le.editingFinished.connect(self.speedChange)
        self.ui.currentHP_le.editingFinished.connect(self.currentHPChange)
        self.ui.totalHitDice_le.editingFinished.connect(self.totalHitDiceChange)
        self.ui.hitDice_le.editingFinished.connect(self.hitDiceChange)
        self.ui.successes1_cb.stateChanged.connect(self.success_ds1Change)
        self.ui.successes2_cb.stateChanged.connect(self.success_ds2Change)
        self.ui.successes3_cb.stateChanged.connect(self.success_ds3Change)
        self.ui.failures1_cb.stateChanged.connect(self.failure_ds1Change)
        self.ui.failures2_cb.stateChanged.connect(self.failure_ds2Change)
        self.ui.failures3_cb.stateChanged.connect(self.failure_ds3Change)
        self.ui.personalityTraits_pte.textChanged.connect(self.personalityTraitsChange)
        self.ui.ideals_pte.textChanged.connect(self.idealsChange)
        self.ui.bonds_pte.textChanged.connect(self.bondsChange)
        self.ui.flaws_pte.textChanged.connect(self.flawsChange)
        self.ui.featuresTraits_pte.textChanged.connect(self.featuresChange)
        self.ui.weapon1Name_le.editingFinished.connect(self.weapon1_nameChange)
        self.ui.weapon2Name_le.editingFinished.connect(self.weapon2_nameChange)
        self.ui.weapon3Name_le.editingFinished.connect(self.weapon3_nameChange)
        self.ui.weapon4Name_le.editingFinished.connect(self.weapon4_nameChange)
        self.ui.weapon1Bonus_sb.valueChanged.connect(self.weapon1_attackChange)
        self.ui.weapon2Bonus_sb.valueChanged.connect(self.weapon2_attackChange)
        self.ui.weapon3Bonus_sb.valueChanged.connect(self.weapon3_attackChange)
        self.ui.weapon4Bonus_sb.valueChanged.connect(self.weapon4_attackChange)
        self.ui.weapon1Damage_le.editingFinished.connect(self.weapon1_damageChange)
        self.ui.weapon2Damage_le.editingFinished.connect(self.weapon2_damageChange)
        self.ui.weapon3Damage_le.editingFinished.connect(self.weapon3_damageChange)
        self.ui.weapon4Damage_le.editingFinished.connect(self.weapon4_damageChange)
        self.ui.weaponInfo_pte.textChanged.connect(self.weapon_infoChange)
        self.ui.languages_pte.textChanged.connect(self.languagesChange)
        self.ui.equipment_pte.textChanged.connect(self.equipmentChange)
        self.ui.notes_pte.textChanged.connect(self.notesChange)
        # ************************************************************************
        
        # Atributes connect
        self.ui.strength_sb.valueChanged.connect(self.showStrModValue)
        self.ui.dexterity_sb.valueChanged.connect(self.showDexModValue)
        self.ui.constitution_sb.valueChanged.connect(self.showConModValue)
        self.ui.intelligence_sb.valueChanged.connect(self.showIntModValue)
        self.ui.wisdom_sb.valueChanged.connect(self.showWisModValue)
        self.ui.charisma_sb.valueChanged.connect(self.showChaModValue)
        self.ui.randomize_btn.pressed.connect(self.randomize)
        # ****************************************************************

        # Menu actions connect
        self.ui.actionSave.triggered.connect(self.save)
        self.ui.actionSave.setShortcut('Ctrl+s')
        self.ui.actionSave_As.triggered.connect(self.saveAs)
        self.ui.actionSave_As.setShortcut('Ctrl+a')
        self.ui.actionLoad.triggered.connect(self.load)
        self.ui.actionLoad.setShortcut('Ctrl+o')
        self.ui.actionNew.triggered.connect(self.new)
        self.ui.actionNew.setShortcut('Ctrl+n')
        # **********************************************

    # takes attr value, returns modifier   
    def getModValue(self, value):
        if value <= 1:
            mod = -5
        elif value == 2 or value == 3:
            mod = -4
        elif value == 4 or value == 5:
            mod = -3
        elif value == 6 or value == 7:
            mod = -2
        elif value == 8 or value == 9:
            mod = -1
        elif value == 10 or value == 11:
            mod = 0
        elif value == 12 or value == 13:
            mod = 1
        elif value == 14 or value == 15:
            mod = 2
        elif value == 16 or value == 17:
            mod = 3
        elif value == 18 or value == 19:
            mod = 4
        elif value == 20 or value == 21:
            mod = 5
        elif value == 22 or value == 23:
            mod = 6
        elif value == 24 or value == 25:
            mod = 7
        elif value == 26 or value == 27:
            mod = 8
        elif value == 28 or value == 29:
            mod = 9
        elif value >= 30:
            mod = 10
        return mod

    # spinbox mod update
    def showStrModValue(self):
        temp = int(self.ui.strength_sb.value())
        modValue = self.getModValue(temp)
        modValue = str(modValue)
        self.character['strength'] = temp
        self.ui.strMod_lb.setText("+ " + modValue)
        self.strSavingThrowChange()
        self.athleticsChange()

    def showDexModValue(self):
        temp = int(self.ui.dexterity_sb.value())
        modValue = self.getModValue(temp)
        modValue = str(modValue)
        self.character['dexterity'] = temp
        self.ui.dexMod_lb.setText("+ " + modValue)
        self.dexSavingThrowChange()
        self.acrobaticsChange()
        self.sleightOfHandChange()
        self.stealthChange()
    
    def showConModValue(self):
        temp = int(self.ui.constitution_sb.value())
        modValue = self.getModValue(temp)
        modValue = str(modValue)
        self.character['constitution'] = temp
        self.ui.conMod_lb.setText("+ " + modValue)
        self.conSavingThrowChange()
        

    def showIntModValue(self):
        temp = int(self.ui.intelligence_sb.value())
        modValue = self.getModValue(temp)
        modValue = str(modValue)
        self.character['intelligence'] = temp
        self.ui.intMod_lb.setText("+ " + modValue)
        self.intSavingThrowChange()
        self.arcanaChange()
        self.historyChange()
        self.investigationChange()
        self.natureChange()
        self.religionChange()
        

    def showWisModValue(self):
        temp = int(self.ui.wisdom_sb.value())
        modValue = self.getModValue(temp)
        modValue = str(modValue)
        self.character['wisdom'] = temp
        self.ui.wisMod_lb.setText("+ " + modValue)
        self.wisSavingThrowChange()
        self.animalHandlingChange()
        self.insightChange()
        self.medicineChange()
        self.perceptionChange()
        self.survivalChange()
        

    def showChaModValue(self):
        temp = int(self.ui.charisma_sb.value())
        modValue = self.getModValue(temp)
        modValue = str(modValue)
        self.character['charisma'] = temp
        self.ui.chaMod_lb.setText("+ " + modValue)
        self.chaSavingThrowChange()
        self.deceptionChange()
        self.intimidationChange()
        self.performanceChange()
        self.persuassionChange()
        
    # **********************************************

    # character dictionary updates
    def characterNameChange(self):
        self.character['character_name'] = self.ui.characterName_le.text()

    def classChange(self):
        self.character['class'] = self.ui.class_combo.currentText()

    def backgroundChange(self):
        self.character['background'] = self.ui.background_le.text()

    def playerNameChange(self):
        self.character['player_name'] = self.ui.playerName_le.text()

    def raceChange(self):
        self.character['race'] = self.ui.race_combo.currentText()

    def alignmentChange(self):
        self.character['alignment'] = self.ui.alignment_combo.currentText()

    def experiencePointsChange(self):
        self.character['experience_points'] = self.ui.xp_le.text()

    def strSavingThrowChange(self):
        self.character['str_saving_throw'] = self.ui.strengthSavingThrow_cb.isChecked()
        if self.ui.strengthSavingThrow_cb.isChecked():
            mod = str(self.getModValue(self.character['strength']))
            self.ui.strengthSavingThrow_cb.setText("+   " + mod)
        else:
            self.ui.strengthSavingThrow_cb.setText("+")

    def dexSavingThrowChange(self):
        self.character['dex_saving_throw'] = self.ui.dexteritySavingThrow_cb.isChecked()
        if self.ui.dexteritySavingThrow_cb.isChecked():
            mod = str(self.getModValue(self.character['dexterity']))
            self.ui.dexteritySavingThrow_cb.setText("+   " + mod)
        else:
            self.ui.dexteritySavingThrow_cb.setText("+")

    def conSavingThrowChange(self):
        self.character['con_saving_throw'] = self.ui.constitutionSavingThrow_cb.isChecked()
        if self.ui.constitutionSavingThrow_cb.isChecked():
            mod = str(self.getModValue(self.character['constitution']))
            self.ui.constitutionSavingThrow_cb.setText("+   " + mod)
        else:
            self.ui.constitutionSavingThrow_cb.setText("+")

    def intSavingThrowChange(self):
        self.character['int_saving_throw'] = self.ui.intelligenceSavingThrow_cb.isChecked()
        if self.ui.intelligenceSavingThrow_cb.isChecked():
            mod = str(self.getModValue(self.character['intelligence']))
            self.ui.intelligenceSavingThrow_cb.setText("+   " + mod)
        else:
            self.ui.intelligenceSavingThrow_cb.setText("+")

    def wisSavingThrowChange(self):
        self.character['wis_saving_throw'] = self.ui.wisdomSavingThrow_cb.isChecked()
        if self.ui.wisdomSavingThrow_cb.isChecked():
            mod = str(self.getModValue(self.character['wisdom']))
            self.ui.wisdomSavingThrow_cb.setText("+   " + mod)
        else:
            self.ui.wisdomSavingThrow_cb.setText("+")

    def chaSavingThrowChange(self):
        self.character['cha_saving_throw'] = self.ui.charismaSavingThrow_cb.isChecked()
        if self.ui.charismaSavingThrow_cb.isChecked():
            mod = str(self.getModValue(self.character['charisma']))
            self.ui.charismaSavingThrow_cb.setText("+   " + mod)
        else: 
            self.ui.charismaSavingThrow_cb.setText("+")

    def acrobaticsChange(self):
        self.character['acrobatics'] = self.ui.acrobatics_cb.isChecked()
        if self.ui.acrobatics_cb.isChecked():
            mod = str(self.getModValue(self.character['dexterity']))
            self.ui.acrobatics_lb.setText(" " + mod + " — Acrobatics (Dex)")
        else:
            self.ui.acrobatics_lb.setText("Acrobatics (Dex)")

    def animalHandlingChange(self):
        self.character['animal_handling'] = self.ui.animalHandling_cb.isChecked()
        if self.ui.animalHandling_cb.isChecked():
            mod = str(self.getModValue(self.character['wisdom']))
            self.ui.animalHandling_lb.setText(" " + mod + " — Animal Handling (Wis)")
        else:
            self.ui.animalHandling_lb.setText("Animal Handling (Wis)")

    def arcanaChange(self):
        self.character['arcana'] = self.ui.arcana_cb.isChecked()
        if self.ui.arcana_cb.isChecked():
            mod = str(self.getModValue(self.character['intelligence']))
            self.ui.arcana_lb.setText(" " + mod + " — Arcana (Int)")
        else:
            self.ui.arcana_lb.setText("Arcana (Int)")

    def athleticsChange(self):
        self.character['athletics'] = self.ui.athletics_cb.isChecked()
        if self.ui.athletics_cb.isChecked():
            mod = str(self.getModValue(self.character['strength']))
            self.ui.athletics_lb.setText(" " + mod + " — Athletics (Str)")
        else:
            self.ui.athletics_lb.setText("Athletics (Str)")

    def deceptionChange(self):
        self.character['deception'] = self.ui.deception_cb.isChecked()
        if self.ui.deception_cb.isChecked():
            mod = str(self.getModValue(self.character['charisma']))
            self.ui.deception_lb.setText(" " + mod + " — Deception (Cha)")
        else:
            self.ui.deception_lb.setText("Deception (Cha)")          

    def historyChange(self):
        self.character['history'] = self.ui.history_cb.isChecked()
        if self.ui.history_cb.isChecked():
            mod = str(self.getModValue(self.character['intelligence']))
            self.ui.history_lb.setText(" " + mod + " — History (Int)")
        else:
            self.ui.history_lb.setText("History (Int)")

    def insightChange(self):
        self.character['insight'] = self.ui.insight_cb.isChecked()
        if self.ui.insight_cb.isChecked():
            mod = str(self.getModValue(self.character['wisdom']))
            self.ui.insight_lb.setText(" " + mod + " — Insight (Wis)")
        else:
            self.ui.insight_lb.setText("Insight (Wis)")

    def intimidationChange(self):
        self.character['intimidation'] = self.ui.intimidation_cb.isChecked()
        if self.ui.intimidation_cb.isChecked():
            mod = str(self.getModValue(self.character['charisma']))
            self.ui.intimidation_lb.setText(" " + mod + " — Intimidation (Cha)")
        else:
            self.ui.intimidation_lb.setText("Intimidation (Cha)")

    def investigationChange(self):
        self.character['investigation'] = self.ui.investigation_cb.isChecked()
        if self.ui.investigation_cb.isChecked():
            mod = str(self.getModValue(self.character['intelligence']))
            self.ui.investigation_lb.setText(" " + mod + " — Investigation (Int)")
        else:
            self.ui.investigation_lb.setText("Investigation (Int)")

    def medicineChange(self):
        self.character['medicine'] = self.ui.medicine_cb.isChecked()
        if self.ui.medicine_cb.isChecked():
            mod = str(self.getModValue(self.character['wisdom']))
            self.ui.medicine_lb.setText(" " + mod + " — Medicine (Wis)")
        else:
            self.ui.medicine_lb.setText("Medicine (Wis)")

    def natureChange(self):
        self.character['nature'] = self.ui.nature_cb.isChecked()
        if self.ui.nature_cb.isChecked():
            mod = str(self.getModValue(self.character['intelligence']))
            self.ui.nature_lb.setText(" " + mod + " — Nature (Int)")
        else:
            self.ui.nature_lb.setText("Nature (Int)")

    def perceptionChange(self):
        self.character['perception'] = self.ui.perception_cb.isChecked()
        if self.ui.perception_cb.isChecked():
            mod = str(self.getModValue(self.character['wisdom']))
            self.ui.perception_lb.setText(" " + mod + " — Perception (Wis)")
        else:
            self.ui.perception_lb.setText("Perception (Wis)")

    def performanceChange(self):
        self.character['performance'] = self.ui.performance_cb.isChecked()
        if self.ui.performance_cb.isChecked():
            mod = str(self.getModValue(self.character['charisma']))
            self.ui.performance_lb.setText(" " + mod + " — Performance (Cha)")
        else:
            self.ui.performance_lb.setText("Performance (Cha)")

    def persuassionChange(self):
        self.character['persuassion'] = self.ui.persuassion_cb.isChecked()
        if self.ui.persuassion_cb.isChecked():
            mod = str(self.getModValue(self.character['charisma']))
            self.ui.persuassion_lb.setText(" " + mod + " — Persuassion (Cha)")
        else:
            self.ui.persuassion_lb.setText("Persuassion (Cha)")

    def religionChange(self):
        self.character['religion'] = self.ui.religion_cb.isChecked()
        if self.ui.religion_cb.isChecked():
            mod = str(self.getModValue(self.character['intelligence']))
            self.ui.religion_lb.setText(" " + mod + " — Religion (Int)")
        else:
            self.ui.religion_lb.setText("Religion (Int)")

    def sleightOfHandChange(self):
        self.character['sleight_of_hand'] = self.ui.sleightOfHand_cb.isChecked()
        if self.ui.sleightOfHand_cb.isChecked():
            mod = str(self.getModValue(self.character['dexterity']))
            self.ui.sleightOfHand_lb.setText(" " + mod + " — Sleight of Hand (Dex)")
        else:
            self.ui.sleightOfHand_lb.setText("Sleight of Hand (Dex)")

    def stealthChange(self):
        self.character['stealth'] = self.ui.stealth_cb.isChecked()
        if self.ui.stealth_cb.isChecked():
            mod = str(self.getModValue(self.character['dexterity']))
            self.ui.stealth_lb.setText(" " + mod + " — Stealth (Dex)")
        else:
            self.ui.stealth_lb.setText("Stealth (Dex)")

    def survivalChange(self):
        self.character['survival'] = self.ui.survival_cb.isChecked()
        if self.ui.survival_cb.isChecked():
            mod = str(self.getModValue(self.character['wisdom']))
            self.ui.survival_lb.setText(" " + mod + " — Survival (Wis)")
        else:
            self.ui.survival_lb.setText("Survival (Wis)")

    def armorClassChange(self):
        self.character['armor_class'] = self.ui.armorClass_le.text()

    def initiativeChange(self):
        self.character['initiative'] = self.ui.initiative_le.text()

    def speedChange(self):
        self.character['speed'] = self.ui.speed_le.text()

    def currentHPChange(self):
        self.character['current_hp'] = self.ui.currentHP_le.text()

    def totalHitDiceChange(self):
        self.character['total_hit_dice'] = self.ui.totalHitDice_le.text()

    def hitDiceChange(self):
        self.character['hit_dice'] = self.ui.hitDice_le.text()

    def success_ds1Change(self):
        self.character['success_ds1'] = self.ui.successes1_cb.isChecked()

    def success_ds2Change(self):
        self.character['success_ds2'] = self.ui.successes2_cb.isChecked()

    def success_ds3Change(self):
        self.character['success_ds3'] = self.ui.successes3_cb.isChecked()

    def failure_ds1Change(self):
        self.character['failure_ds1'] = self.ui.failures1_cb.isChecked()

    def failure_ds2Change(self):
        self.character['failure_ds2'] = self.ui.failures2_cb.isChecked()

    def failure_ds3Change(self):
        self.character['failure_ds3'] = self.ui.failures3_cb.isChecked()

    def personalityTraitsChange(self):
        self.character['personality_traits'] = self.ui.personalityTraits_pte.toPlainText()

    def idealsChange(self):
        self.character['ideals'] = self.ui.ideals_pte.toPlainText()

    def bondsChange(self):
        self.character['bonds'] = self.ui.bonds_pte.toPlainText()

    def flawsChange(self):
        self.character['flaws'] = self.ui.flaws_pte.toPlainText()

    def featuresChange(self):
        self.character['features'] = self.ui.featuresTraits_pte.toPlainText()

    def weapon1_nameChange(self):
        self.character['weapon1_name'] = self.ui.weapon1Name_le.text()

    def weapon2_nameChange(self):
        self.character['weapon2_name'] = self.ui.weapon2Name_le.text()

    def weapon3_nameChange(self):
        self.character['weapon3_name'] = self.ui.weapon3Name_le.text()

    def weapon4_nameChange(self):
        self.character['weapon4_name'] = self.ui.weapon4Name_le.text()

    def weapon1_attackChange(self):
        self.character['weapon1_attack'] = self.ui.weapon1Bonus_sb.value()

    def weapon2_attackChange(self):
        self.character['weapon2_attack'] = self.ui.weapon2Bonus_sb.value()

    def weapon3_attackChange(self):
        self.character['weapon3_attack'] = self.ui.weapon3Bonus_sb.value()

    def weapon4_attackChange(self):
        self.character['weapon4_attack'] = self.ui.weapon4Bonus_sb.value()

    def weapon1_damageChange(self):
        self.character['weapon1_type'] = self.ui.weapon1Damage_le.text()

    def weapon2_damageChange(self):
        self.character['weapon2_type'] = self.ui.weapon2Damage_le.text()

    def weapon3_damageChange(self):
        self.character['weapon3_type'] = self.ui.weapon3Damage_le.text()

    def weapon4_damageChange(self):
        self.character['weapon4_type'] = self.ui.weapon4Damage_le.text()

    def weapon_infoChange(self):
        self.character['weapon_info'] = self.ui.weaponInfo_pte.toPlainText()

    def languagesChange(self):
        self.character['languages'] = self.ui.languages_pte.toPlainText()

    def featuresTraitsChange(self):
        self.character['features'] = self.ui.featuresTraits_pte.toPlainText()

    def equipmentChange(self):
        self.character['equipment'] = self.ui.equipment_pte.toPlainText()

    def notesChange(self):
        self.character['notes'] = self.ui.notes_pte.toPlainText()

    # *********************************************

    # randomization operations
    def getRandomStat(self):
        dice_list = list()

        dice_1 = randint(1, 6)
        dice_2 = randint(1, 6)
        dice_3 = randint(1, 6)
        dice_4 = randint(1,6)

        dice_list.append(dice_1)
        dice_list.append(dice_2)
        dice_list.append(dice_3)
        dice_list.append(dice_4)

        dice_list = sorted(dice_list)
        dice_list = dice_list[::-1]

        total = dice_list[0] + dice_list[1] + dice_list[2]
        
        return total

    def randomize(self):
        randStr = self.getRandomStat()
        randDex = self.getRandomStat()
        randCon = self.getRandomStat()
        randInt = self.getRandomStat()
        randWis = self.getRandomStat()
        randCha = self.getRandomStat()

        self.character['strength'] = randStr
        self.character['dexterity'] = randDex
        self.character['constitution'] = randCon
        self.character['intelligence'] = randInt
        self.character['wisdom'] = randWis
        self.character['charisma'] = randCha
        self.refresh() 
        self.statusBar().showMessage('Atributes randomized.')

    # **********************************************

    # file operations
    def save(self):
        if self.filename:
            file = open(self.filename, 'w')
            json.dump(self.character, file)
            file.close()
            self.statusBar().showMessage('File saved.')
            self.refresh()
        else:
            self.saveAs()

    def saveAs(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.filename, _ = QFileDialog.getSaveFileName(self,'Save File', '.txt','Text Files (*.txt)', options=options)
        if '.txt' not in self.filename:
            self.filename = self.filename + '.txt'
        if self.filename:
            file = open(self.filename, 'w')
            json.dump(self.character, file)
            file.close()
            self.refresh()
            self.statusBar().showMessage('File saved.')

    def load(self):
        self.character = self.characterTemplate
        self.refresh()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.filename, _ = QFileDialog.getOpenFileName(self,'Open File', '','Text Files (*.txt)', options=options)
        if self.filename:
            file = open(self.filename, 'r')
            json_data = json.load(file)
            self.character = json_data
            file.close()
            self.refresh()
            self.statusBar().showMessage('File loaded.')
            

    def new(self):
        msg = QMessageBox()
        msg.setGeometry(10, 10, 320, 200)
        buttonReply = QMessageBox.question(self, 'DnD Notepad', 'Create new character? Unsaved changes will be lost.', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        msg.show()
        if buttonReply == QMessageBox.Yes:
            self.filename = ''
            self.character = self.characterTemplate
            self.refresh()
            self.statusBar().showMessage('New character created.')
        else:
            return
        
    def refresh(self):
        self.ui.characterName_le.setText(self.character['character_name'])
        self.ui.class_combo.setCurrentText(self.character['class'])
        self.ui.background_le.setText(self.character['background'])
        self.ui.playerName_le.setText(self.character['player_name'])
        self.ui.race_combo.setCurrentText(self.character['race'])
        self.ui.alignment_combo.setCurrentText(self.character['alignment'])
        self.ui.xp_le.setText(str(self.character['experience_points']))
        self.ui.strength_sb.setValue(self.character['strength'])
        self.ui.dexterity_sb.setValue(self.character['dexterity'])
        self.ui.constitution_sb.setValue(self.character['constitution'])
        self.ui.intelligence_sb.setValue(self.character['intelligence'])
        self.ui.wisdom_sb.setValue(self.character['wisdom'])
        self.ui.charisma_sb.setValue(self.character['charisma'])
        self.ui.strengthSavingThrow_cb.setChecked(self.character['str_saving_throw'])
        self.ui.dexteritySavingThrow_cb.setChecked(self.character['dex_saving_throw'])
        self.ui.constitutionSavingThrow_cb.setChecked(self.character['con_saving_throw'])
        self.ui.intelligenceSavingThrow_cb.setChecked(self.character['int_saving_throw'])
        self.ui.wisdomSavingThrow_cb.setChecked(self.character['wis_saving_throw'])
        self.ui.charismaSavingThrow_cb.setChecked(self.character['cha_saving_throw'])
        self.ui.acrobatics_cb.setChecked(self.character['acrobatics'])
        self.ui.animalHandling_cb.setChecked(self.character['animal_handling'])
        self.ui.arcana_cb.setChecked(self.character['arcana'])
        self.ui.athletics_cb.setChecked(self.character['athletics'])
        self.ui.deception_cb.setChecked(self.character['deception'])
        self.ui.history_cb.setChecked(self.character['history'])
        self.ui.insight_cb.setChecked(self.character['insight'])
        self.ui.intimidation_cb.setChecked(self.character['intimidation'])
        self.ui.investigation_cb.setChecked(self.character['investigation'])
        self.ui.medicine_cb.setChecked(self.character['medicine'])
        self.ui.nature_cb.setChecked(self.character['nature'])
        self.ui.perception_cb.setChecked(self.character['perception'])
        self.ui.performance_cb.setChecked(self.character['performance'])
        self.ui.persuassion_cb.setChecked(self.character['persuassion'])
        self.ui.religion_cb.setChecked(self.character['religion'])
        self.ui.sleightOfHand_cb.setChecked(self.character['sleight_of_hand'])
        self.ui.stealth_cb.setChecked(self.character['stealth'])
        self.ui.survival_cb.setChecked(self.character['survival'])
        self.ui.armorClass_le.setText(str(self.character['armor_class']))
        self.ui.initiative_le.setText(str(self.character['initiative']))
        self.ui.speed_le.setText(str(self.character['speed']))
        self.ui.currentHP_le.setText(str(self.character['current_hp']))
        self.ui.totalHitDice_le.setText(str(self.character['total_hit_dice']))
        self.ui.hitDice_le.setText(str(self.character['hit_dice']))
        self.ui.successes1_cb.setChecked(self.character['success_ds1'])
        self.ui.successes2_cb.setChecked(self.character['success_ds2'])
        self.ui.successes3_cb.setChecked(self.character['success_ds3'])
        self.ui.failures1_cb.setChecked(self.character['failure_ds1'])
        self.ui.failures2_cb.setChecked(self.character['failure_ds2'])
        self.ui.failures3_cb.setChecked(self.character['failure_ds3'])
        self.ui.personalityTraits_pte.setPlainText(self.character['personality_traits'])
        self.ui.ideals_pte.setPlainText(self.character['ideals'])
        self.ui.bonds_pte.setPlainText(self.character['bonds'])
        self.ui.flaws_pte.setPlainText(self.character['flaws'])
        self.ui.featuresTraits_pte.setPlainText(self.character['features'])
        self.ui.weapon1Name_le.setText(self.character['weapon1_name'])
        self.ui.weapon2Name_le.setText(self.character['weapon2_name'])
        self.ui.weapon3Name_le.setText(self.character['weapon3_name'])
        self.ui.weapon4Name_le.setText(self.character['weapon4_name'])
        self.ui.weapon1Bonus_sb.setValue(self.character['weapon1_attack'])
        self.ui.weapon2Bonus_sb.setValue(self.character['weapon2_attack'])
        self.ui.weapon3Bonus_sb.setValue(self.character['weapon3_attack'])
        self.ui.weapon4Bonus_sb.setValue(self.character['weapon4_attack'])
        self.ui.weapon1Damage_le.setText(self.character['weapon1_type'])
        self.ui.weapon2Damage_le.setText(self.character['weapon2_type'])
        self.ui.weapon3Damage_le.setText(self.character['weapon3_type'])
        self.ui.weapon4Damage_le.setText(self.character['weapon4_type'])
        self.ui.weaponInfo_pte.setPlainText(self.character['weapon_info'])
        self.ui.languages_pte.setPlainText(self.character['languages'])
        self.ui.equipment_pte.setPlainText(self.character['equipment'])
        self.ui.notes_pte.setPlainText(self.character['notes'])
    # *************************************************************************

# driver
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
	