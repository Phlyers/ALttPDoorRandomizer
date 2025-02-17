from test.owg.TestVanillaOWG import TestVanillaOWG


class TestDeathMountain(TestVanillaOWG):

    def testWestDeathMountain(self):
        self.run_location_tests([
            ["Ether Tablet", False, []],
            ["Ether Tablet", False, ['Progressive Sword'], ['Progressive Sword']],
            ["Ether Tablet", False, [], ['Book of Mudora']],
            ["Ether Tablet", False, [], ['Pegasus Boots', 'Progressive Glove', 'Ocarina']],
            ["Ether Tablet", False, [], ['Pegasus Boots', 'Lamp', 'Ocarina']],
            ["Ether Tablet", False, [], ['Pegasus Boots', 'Magic Mirror', 'Hookshot']],
            ["Ether Tablet", False, [], ['Pegasus Boots', 'Magic Mirror', 'Hammer']],
            ["Ether Tablet", True, ['Pegasus Boots', 'Book of Mudora', 'Progressive Sword', 'Progressive Sword']],
            ["Ether Tablet", True, ['Ocarina', 'Magic Mirror', 'Book of Mudora', 'Progressive Sword', 'Progressive Sword']],
            ["Ether Tablet", True, ['Progressive Glove', 'Lamp', 'Magic Mirror', 'Book of Mudora', 'Progressive Sword', 'Progressive Sword']],
            ["Ether Tablet", True, ['Ocarina', 'Hammer', 'Hookshot', 'Book of Mudora', 'Progressive Sword', 'Progressive Sword']],
            ["Ether Tablet", True, ['Progressive Glove', 'Lamp', 'Hammer', 'Hookshot', 'Book of Mudora', 'Progressive Sword', 'Progressive Sword']],

            ["Old Man", False, []],
            ["Old Man", False, [], ['Lamp']],
            ["Old Man", False, [], ['Pegasus Boots', 'Progressive Glove', 'Ocarina']],
            ["Old Man", True, ['Pegasus Boots', 'Lamp']],
            ["Old Man", True, ['Ocarina', 'Lamp']],
            ["Old Man", True, ['Progressive Glove', 'Lamp']],

            ["Spectacle Rock Cave", False, []],
            ["Spectacle Rock Cave", False, [], ['Pegasus Boots', 'Progressive Glove', 'Ocarina']],
            ["Spectacle Rock Cave", False, [], ['Pegasus Boots', 'Lamp', 'Ocarina']],
            ["Spectacle Rock Cave", True, ['Pegasus Boots']],
            ["Spectacle Rock Cave", True, ['Ocarina']],
            ["Spectacle Rock Cave", True, ['Progressive Glove', 'Lamp']],

            ["Spectacle Rock", False, []],
            ["Spectacle Rock", False, [], ['Pegasus Boots', 'Progressive Glove', 'Ocarina']],
            ["Spectacle Rock", False, [], ['Pegasus Boots', 'Lamp', 'Ocarina']],
            ["Spectacle Rock", False, [], ['Pegasus Boots', 'Magic Mirror']],
            ["Spectacle Rock", True, ['Pegasus Boots']],
            ["Spectacle Rock", True, ['Ocarina', 'Magic Mirror']],
            ["Spectacle Rock", True, ['Progressive Glove', 'Lamp', 'Magic Mirror']],
        ])

    def testEastDeathMountain(self):
        self.run_location_tests([
            ["Mimic Cave", False, []],
            ["Mimic Cave", False, [], ['Magic Mirror']],
            ["Mimic Cave", False, [], ['Hammer']],
            ["Mimic Cave", False, [], ['Pegasus Boots', 'Ocarina', 'Lamp']],
            ["Mimic Cave", False, [], ['Pegasus Boots', 'Ocarina', 'Progressive Glove']],
            ["Mimic Cave", True, ['Magic Mirror', 'Hammer', 'Pegasus Boots']],
            ["Mimic Cave", True, ['Magic Mirror', 'Hammer', 'Progressive Glove', 'Lamp']],
            ["Mimic Cave", True, ['Magic Mirror', 'Hammer', 'Ocarina']],

            ["Spiral Cave", False, []],
            ["Spiral Cave", False, [], ['Pegasus Boots', 'Progressive Glove', 'Ocarina']],
            ["Spiral Cave", False, [], ['Pegasus Boots', 'Magic Mirror', 'Hookshot']],
            ["Spiral Cave", True, ['Pegasus Boots']],
            ["Spiral Cave", True, ['Ocarina', 'Hookshot']],
            ["Spiral Cave", True, ['Progressive Glove', 'Lamp', 'Hookshot']],
            ["Spiral Cave", True, ['Progressive Glove', 'Lamp', 'Magic Mirror']],
            ["Spiral Cave", True, ['Ocarina', 'Magic Mirror']],

            ["Paradox Cave Lower - Far Left", False, []],
            ["Paradox Cave Lower - Far Left", False, [], ['Pegasus Boots', 'Progressive Glove', 'Ocarina']],
            ["Paradox Cave Lower - Far Left", False, [], ['Pegasus Boots', 'Magic Mirror', 'Hookshot']],
            ["Paradox Cave Lower - Far Left", True, ['Pegasus Boots']],
            ["Paradox Cave Lower - Far Left", True, ['Ocarina', 'Hookshot']],
            ["Paradox Cave Lower - Far Left", True, ['Progressive Glove', 'Lamp', 'Hookshot']],
            ["Paradox Cave Lower - Far Left", True, ['Progressive Glove', 'Lamp', 'Magic Mirror']],
            ["Paradox Cave Lower - Far Left", True, ['Ocarina', 'Magic Mirror']],

            ["Paradox Cave Lower - Left", False, []],
            ["Paradox Cave Lower - Left", False, [], ['Pegasus Boots', 'Progressive Glove', 'Ocarina']],
            ["Paradox Cave Lower - Left", False, [], ['Pegasus Boots', 'Magic Mirror', 'Hookshot']],
            ["Paradox Cave Lower - Left", True, ['Pegasus Boots']],
            ["Paradox Cave Lower - Left", True, ['Ocarina', 'Hookshot']],
            ["Paradox Cave Lower - Left", True, ['Progressive Glove', 'Lamp', 'Hookshot']],
            ["Paradox Cave Lower - Left", True, ['Progressive Glove', 'Lamp', 'Magic Mirror']],
            ["Paradox Cave Lower - Left", True, ['Ocarina', 'Magic Mirror']],

            ["Paradox Cave Lower - Middle", False, []],
            ["Paradox Cave Lower - Middle", False, [], ['Pegasus Boots', 'Progressive Glove', 'Ocarina']],
            ["Paradox Cave Lower - Middle", False, [], ['Pegasus Boots', 'Magic Mirror', 'Hookshot']],
            ["Paradox Cave Lower - Middle", True, ['Pegasus Boots']],
            ["Paradox Cave Lower - Middle", True, ['Ocarina', 'Hookshot']],
            ["Paradox Cave Lower - Middle", True, ['Progressive Glove', 'Lamp', 'Hookshot']],
            ["Paradox Cave Lower - Middle", True, ['Progressive Glove', 'Lamp', 'Magic Mirror']],
            ["Paradox Cave Lower - Middle", True, ['Ocarina', 'Magic Mirror']],

            ["Paradox Cave Lower - Right", False, []],
            ["Paradox Cave Lower - Right", False, [], ['Pegasus Boots', 'Progressive Glove', 'Ocarina']],
            ["Paradox Cave Lower - Right", False, [], ['Pegasus Boots', 'Magic Mirror', 'Hookshot']],
            ["Paradox Cave Lower - Right", True, ['Pegasus Boots']],
            ["Paradox Cave Lower - Right", True, ['Ocarina', 'Hookshot']],
            ["Paradox Cave Lower - Right", True, ['Progressive Glove', 'Lamp', 'Hookshot']],
            ["Paradox Cave Lower - Right", True, ['Progressive Glove', 'Lamp', 'Magic Mirror']],
            ["Paradox Cave Lower - Right", True, ['Ocarina', 'Magic Mirror']],

            ["Paradox Cave Lower - Far Right", False, []],
            ["Paradox Cave Lower - Far Right", False, [], ['Pegasus Boots', 'Progressive Glove', 'Ocarina']],
            ["Paradox Cave Lower - Far Right", False, [], ['Pegasus Boots', 'Magic Mirror', 'Hookshot']],
            ["Paradox Cave Lower - Far Right", True, ['Pegasus Boots']],
            ["Paradox Cave Lower - Far Right", True, ['Ocarina', 'Hookshot']],
            ["Paradox Cave Lower - Far Right", True, ['Progressive Glove', 'Lamp', 'Hookshot']],
            ["Paradox Cave Lower - Far Right", True, ['Progressive Glove', 'Lamp', 'Magic Mirror']],
            ["Paradox Cave Lower - Far Right", True, ['Ocarina', 'Magic Mirror']],

            ["Paradox Cave Upper - Left", False, []],
            ["Paradox Cave Upper - Left", False, [], ['Pegasus Boots', 'Progressive Glove', 'Ocarina']],
            ["Paradox Cave Upper - Left", False, [], ['Pegasus Boots', 'Magic Mirror', 'Hookshot']],
            ["Paradox Cave Upper - Left", True, ['Pegasus Boots']],
            ["Paradox Cave Upper - Left", True, ['Ocarina', 'Hookshot']],
            ["Paradox Cave Upper - Left", True, ['Progressive Glove', 'Lamp', 'Hookshot']],
            ["Paradox Cave Upper - Left", True, ['Progressive Glove', 'Lamp', 'Magic Mirror']],
            ["Paradox Cave Upper - Left", True, ['Ocarina', 'Magic Mirror']],

            ["Paradox Cave Upper - Right", False, []],
            ["Paradox Cave Upper - Right", False, [], ['Pegasus Boots', 'Progressive Glove', 'Ocarina']],
            ["Paradox Cave Upper - Right", False, [], ['Pegasus Boots', 'Magic Mirror', 'Hookshot']],
            ["Paradox Cave Upper - Right", True, ['Pegasus Boots']],
            ["Paradox Cave Upper - Right", True, ['Ocarina', 'Hookshot']],
            ["Paradox Cave Upper - Right", True, ['Progressive Glove', 'Lamp', 'Hookshot']],
            ["Paradox Cave Upper - Right", True, ['Progressive Glove', 'Lamp', 'Magic Mirror']],
            ["Paradox Cave Upper - Right", True, ['Ocarina', 'Magic Mirror']],
        ])

    def testWestDarkWorldDeathMountain(self):
        self.run_location_tests([
            ["Spike Cave", False, []],
            ["Spike Cave", False, [], ['Progressive Glove']],
            ["Spike Cave", False, [], ['Moon Pearl']],
            ["Spike Cave", False, [], ['Hammer']],
            ["Spike Cave", False, [], ['Cape', 'Cane of Byrna']],
            ["Spike Cave", True, ['Bottle', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Lamp', 'Cape']],
            ["Spike Cave", True, ['Bottle', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Ocarina', 'Cape']],
            ["Spike Cave", True, ['Bottle', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Lamp', 'Cane of Byrna']],
            ["Spike Cave", True, ['Bottle', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Ocarina', 'Cane of Byrna']],
            ["Spike Cave", True, ['Magic Upgrade (1/2)', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Lamp', 'Cape']],
            ["Spike Cave", True, ['Magic Upgrade (1/2)', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Ocarina', 'Cape']],
            ["Spike Cave", True, ['Magic Upgrade (1/2)', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Lamp', 'Cane of Byrna']],
            ["Spike Cave", True, ['Magic Upgrade (1/2)', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Ocarina', 'Cane of Byrna']],
            ["Spike Cave", True, ['Magic Upgrade (1/4)', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Lamp', 'Cape']],
            ["Spike Cave", True, ['Magic Upgrade (1/4)', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Ocarina', 'Cape']],
            ["Spike Cave", True, ['Magic Upgrade (1/4)', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Lamp', 'Cane of Byrna']],
            ["Spike Cave", True, ['Magic Upgrade (1/4)', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Ocarina', 'Cane of Byrna']],
        ])

    def testEastDarkWorldDeathMountain(self):
        self.run_location_tests([
            ["Superbunny Cave - Top", False, []],
            ["Superbunny Cave - Top", True, ['Progressive Glove', 'Progressive Glove', 'Pegasus Boots']],
            ["Superbunny Cave - Top", True, ['Hammer', 'Pegasus Boots']],
            ["Superbunny Cave - Top", True, ['Moon Pearl', 'Pegasus Boots']],
            ["Superbunny Cave - Top", True, ['Progressive Glove', 'Progressive Glove', 'Hookshot', 'Ocarina']],
            ["Superbunny Cave - Top", True, ['Progressive Glove', 'Progressive Glove', 'Magic Mirror', 'Hammer', 'Ocarina']],
            ["Superbunny Cave - Top", True, ['Progressive Glove', 'Progressive Glove', 'Hookshot', 'Lamp']],
            ["Superbunny Cave - Top", True, ['Progressive Glove', 'Progressive Glove', 'Magic Mirror', 'Hammer', 'Lamp']],

            ["Superbunny Cave - Bottom", False, []],
            ["Superbunny Cave - Bottom", True, ['Progressive Glove', 'Progressive Glove', 'Pegasus Boots']],
            ["Superbunny Cave - Bottom", True, ['Hammer', 'Pegasus Boots']],
            ["Superbunny Cave - Bottom", True, ['Moon Pearl', 'Pegasus Boots']],
            ["Superbunny Cave - Bottom", True, ['Progressive Glove', 'Progressive Glove', 'Hookshot', 'Ocarina']],
            ["Superbunny Cave - Bottom", True, ['Progressive Glove', 'Progressive Glove', 'Magic Mirror', 'Hammer', 'Ocarina']],
            ["Superbunny Cave - Bottom", True, ['Progressive Glove', 'Progressive Glove', 'Hookshot', 'Lamp']],
            ["Superbunny Cave - Bottom", True, ['Progressive Glove', 'Progressive Glove', 'Magic Mirror', 'Hammer', 'Lamp']],

            ["Hookshot Cave - Bottom Right", False, []],
            ["Hookshot Cave - Bottom Right", False, [], ['Progressive Glove', 'Pegasus Boots']],
            ["Hookshot Cave - Bottom Right", False, [], ['Moon Pearl']],
            ["Hookshot Cave - Bottom Right", True, ['Moon Pearl', 'Pegasus Boots']],
            ["Hookshot Cave - Bottom Right", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Ocarina']],
            ["Hookshot Cave - Bottom Right", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Magic Mirror', 'Hammer', 'Ocarina', 'Pegasus Boots']],
            ["Hookshot Cave - Bottom Right", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Lamp']],
            ["Hookshot Cave - Bottom Right", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Magic Mirror', 'Hammer', 'Lamp', 'Pegasus Boots']],

            ["Hookshot Cave - Bottom Left", False, []],
            ["Hookshot Cave - Bottom Left", False, [], ['Progressive Glove', 'Pegasus Boots']],
            ["Hookshot Cave - Bottom Left", False, [], ['Moon Pearl']],
            ["Hookshot Cave - Bottom Left", False, [], ['Hookshot']],
            ["Hookshot Cave - Bottom Left", True, ['Moon Pearl', 'Pegasus Boots', 'Hookshot']],
            ["Hookshot Cave - Bottom Left", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Ocarina']],
            ["Hookshot Cave - Bottom Left", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Lamp']],

            ["Hookshot Cave - Top Left", False, []],
            ["Hookshot Cave - Top Left", False, [], ['Progressive Glove', 'Pegasus Boots']],
            ["Hookshot Cave - Top Left", False, [], ['Moon Pearl']],
            ["Hookshot Cave - Top Left", False, [], ['Hookshot']],
            ["Hookshot Cave - Top Left", True, ['Moon Pearl', 'Pegasus Boots', 'Hookshot']],
            ["Hookshot Cave - Top Left", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Ocarina']],
            ["Hookshot Cave - Top Left", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Lamp']],

            ["Hookshot Cave - Top Right", False, []],
            ["Hookshot Cave - Top Right", False, [], ['Progressive Glove', 'Pegasus Boots']],
            ["Hookshot Cave - Top Right", False, [], ['Moon Pearl']],
            ["Hookshot Cave - Top Right", False, [], ['Hookshot']],
            ["Hookshot Cave - Top Right", True, ['Moon Pearl', 'Pegasus Boots', 'Hookshot']],
            ["Hookshot Cave - Top Right", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Ocarina']],
            ["Hookshot Cave - Top Right", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Lamp']],
        ])