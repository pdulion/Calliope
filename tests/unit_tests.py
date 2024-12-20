import time
import unittest
from calliope.frequency_note_conversion import freq_to_note, note_to_freq



class MyTestCase(unittest.TestCase):
    def test_frequency_to_note(self):
        self.assertEqual("A0", freq_to_note(27.5000))  # A0
        self.assertEqual("A#0", freq_to_note(29.1352))  # A#0
        self.assertEqual("B0", freq_to_note(30.8677))  # B0
        self.assertEqual("C1", freq_to_note(32.7032))  # C1
        self.assertEqual("C#1", freq_to_note(34.6478))  # C#1
        self.assertEqual("D1", freq_to_note(36.7081))  # D1
        self.assertEqual("D#1", freq_to_note(38.8909))  # D#1
        self.assertEqual("E1", freq_to_note(41.2034))  # E1
        self.assertEqual("F1", freq_to_note(43.6535))  # F1
        self.assertEqual("F#1", freq_to_note(46.2493))  # F#1
        self.assertEqual("G1", freq_to_note(49.0000))  # G1
        self.assertEqual("G#1", freq_to_note(51.9131))  # G#1
        self.assertEqual("A1", freq_to_note(55.0000))  # A1
        self.assertEqual("A#1", freq_to_note(58.2705))  # A#1
        self.assertEqual("B1", freq_to_note(61.7354))  # B1
        self.assertEqual("C2", freq_to_note(65.4064))  # C2
        self.assertEqual("C#2", freq_to_note(69.2957))  # C#2
        self.assertEqual("D2", freq_to_note(73.4162))  # D2
        self.assertEqual("D#2", freq_to_note(77.7817))  # D#2
        self.assertEqual("E2", freq_to_note(82.4069))  # E2
        self.assertEqual("F2", freq_to_note(87.3071))  # F2
        self.assertEqual("F#2", freq_to_note(92.4986))  # F#2
        self.assertEqual("G2", freq_to_note(98.0000))  # G2
        self.assertEqual("G#2", freq_to_note(103.8261))  # G#2
        self.assertEqual("A2", freq_to_note(110.0000))  # A2
        self.assertEqual("A#2", freq_to_note(116.5409))  # A#2
        self.assertEqual("B2", freq_to_note(123.4708))  # B2
        self.assertEqual("C3", freq_to_note(130.8128))  # C3
        self.assertEqual("C#3", freq_to_note(138.5913))  # C#3
        self.assertEqual("D3", freq_to_note(146.8324))  # D3
        self.assertEqual("D#3", freq_to_note(155.5635))  # D#3
        self.assertEqual("E3", freq_to_note(164.8138))  # E3
        self.assertEqual("F3", freq_to_note(174.6141))  # F3
        self.assertEqual("F#3", freq_to_note(184.9972))  # F#3
        self.assertEqual("G3", freq_to_note(196.0000))  # G3
        self.assertEqual("G#3", freq_to_note(207.6523))  # G#3
        self.assertEqual("A3", freq_to_note(220.0000))  # A3
        self.assertEqual("A#3", freq_to_note(233.0819))  # A#3
        self.assertEqual("B3", freq_to_note(246.9417))  # B3
        self.assertEqual("C4", freq_to_note(261.6256))  # C4
        self.assertEqual("C#4", freq_to_note(277.1826))  # C#4
        self.assertEqual("D4", freq_to_note(293.6648))  # D4
        self.assertEqual("D#4", freq_to_note(311.1270))  # D#4
        self.assertEqual("E4", freq_to_note(329.6276))  # E4
        self.assertEqual("F4", freq_to_note(349.2282))  # F4
        self.assertEqual("F#4", freq_to_note(369.9944))  # F#4
        self.assertEqual("G4", freq_to_note(392.0000))  # G4
        self.assertEqual("G#4", freq_to_note(415.3047))  # G#4
        self.assertEqual("A4", freq_to_note(440.0000))  # A4
        self.assertEqual("A#4", freq_to_note(466.1638))  # A#4
        self.assertEqual("B4", freq_to_note(493.8833))  # B4
        self.assertEqual("C5", freq_to_note(523.2519))  # C5
        self.assertEqual("C#5", freq_to_note(554.3653))  # C#5
        self.assertEqual("D5", freq_to_note(587.3295))  # D5
        self.assertEqual("D#5", freq_to_note(622.2539))  # D#5
        self.assertEqual("E5", freq_to_note(659.2551))  # E5
        self.assertEqual("F5", freq_to_note(698.4565))  # F5
        self.assertEqual("F#5", freq_to_note(739.9888))  # F#5
        self.assertEqual("G5", freq_to_note(783.9909))  # G5
        self.assertEqual("G#5", freq_to_note(830.6094))  # G#5
        self.assertEqual("A5", freq_to_note(880.0000))  # A5
        self.assertEqual("A#5", freq_to_note(932.3275))  # A#5
        self.assertEqual("B5", freq_to_note(987.7666))  # B5
        self.assertEqual("C6", freq_to_note(1046.5023))  # C6
        self.assertEqual("C#6", freq_to_note(1108.7305))  # C#6
        self.assertEqual("D6", freq_to_note(1174.6591))  # D6
        self.assertEqual("D#6", freq_to_note(1244.5079))  # D#6
        self.assertEqual("E6", freq_to_note(1318.5109))  # E6
        self.assertEqual("F6", freq_to_note(1396.9129))  # F6
        self.assertEqual("F#6", freq_to_note(1479.9771))  # F#6
        self.assertEqual("G6", freq_to_note(1567.9817))  # G6
        self.assertEqual("G#6", freq_to_note(1661.2180))  # G#6
        self.assertEqual("A6", freq_to_note(1760.0000))  # A6
        self.assertEqual("A#6", freq_to_note(1864.6550))  # A#6
        self.assertEqual("B6", freq_to_note(1975.5339))  # B6
        self.assertEqual("C7", freq_to_note(2093.0045))  # C7
        self.assertEqual("C#7", freq_to_note(2217.4610))  # C#7
        self.assertEqual("D7", freq_to_note(2349.3181))  # D7
        self.assertEqual("D#7", freq_to_note(2489.0160))  # D#7
        self.assertEqual("E7", freq_to_note(2637.0205))  # E7
        self.assertEqual("F7", freq_to_note(2793.8259))  # F7
        self.assertEqual("F#7", freq_to_note(2959.9554))  # F#7
        self.assertEqual("G7", freq_to_note(3135.9635))  # G7
        self.assertEqual("G#7", freq_to_note(3322.4376))  # G#7
        self.assertEqual("A7", freq_to_note(3520.0000))  # A7
        self.assertEqual("A#7", freq_to_note(3729.3100))  # A#7
        self.assertEqual("B7", freq_to_note(3951.0660))  # B7
        self.assertEqual("C8", freq_to_note(4186.0090))  # C8

    def test_note_to_frequency(self):
        self.assertAlmostEqual(27.5000, note_to_freq("A0"), places=1)  # A0
        self.assertAlmostEqual(29.1352, note_to_freq("A#0"), places=1)  # A#0
        self.assertAlmostEqual(30.8677, note_to_freq("B0"), places=1)  # B0
        self.assertAlmostEqual(32.7032, note_to_freq("C1"), places=1)  # C1
        self.assertAlmostEqual(34.6478, note_to_freq("C#1"), places=1)  # C#1
        self.assertAlmostEqual(36.7081, note_to_freq("D1"), places=1)  # D1
        self.assertAlmostEqual(38.8909, note_to_freq("D#1"), places=1)  # D#1
        self.assertAlmostEqual(41.2034, note_to_freq("E1"), places=1)  # E1
        self.assertAlmostEqual(43.6535, note_to_freq("F1"), places=1)  # F1
        self.assertAlmostEqual(46.2493, note_to_freq("F#1"), places=1)  # F#1
        self.assertAlmostEqual(49.0000, note_to_freq("G1"), places=1)  # G1
        self.assertAlmostEqual(51.9131, note_to_freq("G#1"), places=1)  # G#1
        self.assertAlmostEqual(55.0000, note_to_freq("A1"), places=1)  # A1
        self.assertAlmostEqual(58.2705, note_to_freq("A#1"), places=1)  # A#1


        self.assertAlmostEqual(440.0000, note_to_freq("A4"), places=1) #A4

        self.assertAlmostEqual(261.6256, note_to_freq("C4"), places=1)  # C4

if __name__ == '__main__':
    unittest.main()
