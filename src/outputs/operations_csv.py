

import os
import csv
import logging
logger = logging.getLogger("outputs")


def generate(agent, output_folder):
    logger.info("Generating CSV Output for Operations in {}".format(output_folder))
    with open(os.path.join(output_folder, 'manufacturing_operations.csv'), 'w') as outfile:
        writer = csv.DictWriter(outfile, ('Operation', 'Machine', 'Coach Variant',
                                          'Start Time', 'End Time',
                                          'Input', 'Output',
                                          'Coach Variant Manufactured'))
        writer.writeheader()
        writer.writerows(agent.schedule)
