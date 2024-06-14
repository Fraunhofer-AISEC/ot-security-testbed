#!/usr/bin/env python3
#                                  Apache License
#                            Version 2.0, January 2004
#                         http://www.apache.org/licenses/
#
#    TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
#
#    1. Definitions.
#
#       "License" shall mean the terms and conditions for use, reproduction,
#       and distribution as defined by Sections 1 through 9 of this document.
#
#       "Licensor" shall mean the copyright owner or entity authorized by
#       the copyright owner that is granting the License.
#
#       "Legal Entity" shall mean the union of the acting entity and all
#       other entities that control, are controlled by, or are under common
#       control with that entity. For the purposes of this definition,
#       "control" means (i) the power, direct or indirect, to cause the
#       direction or management of such entity, whether by contract or
#       otherwise, or (ii) ownership of fifty percent (50%) or more of the
#       outstanding shares, or (iii) beneficial ownership of such entity.
#
#       "You" (or "Your") shall mean an individual or Legal Entity
#       exercising permissions granted by this License.
#
#       "Source" form shall mean the preferred form for making modifications,
#       including but not limited to software source code, documentation
#       source, and configuration files.
#
#       "Object" form shall mean any form resulting from mechanical
#       transformation or translation of a Source form, including but
#       not limited to compiled object code, generated documentation,
#       and conversions to other media types.
#
#       "Work" shall mean the work of authorship, whether in Source or
#       Object form, made available under the License, as indicated by a
#       copyright notice that is included in or attached to the work
#       (an example is provided in the Appendix below).
#
#       "Derivative Works" shall mean any work, whether in Source or Object
#       form, that is based on (or derived from) the Work and for which the
#       editorial revisions, annotations, elaborations, or other modifications
#       represent, as a whole, an original work of authorship. For the purposes
#       of this License, Derivative Works shall not include works that remain
#       separable from, or merely link (or bind by name) to the interfaces of,
#       the Work and Derivative Works thereof.
#
#       "Contribution" shall mean any work of authorship, including
#       the original version of the Work and any modifications or additions
#       to that Work or Derivative Works thereof, that is intentionally
#       submitted to Licensor for inclusion in the Work by the copyright owner
#       or by an individual or Legal Entity authorized to submit on behalf of
#       the copyright owner. For the purposes of this definition, "submitted"
#       means any form of electronic, verbal, or written communication sent
#       to the Licensor or its representatives, including but not limited to
#       communication on electronic mailing lists, source code control systems,
#       and issue tracking systems that are managed by, or on behalf of, the
#       Licensor for the purpose of discussing and improving the Work, but
#       excluding communication that is conspicuously marked or otherwise
#       designated in writing by the copyright owner as "Not a Contribution."
#
#       "Contributor" shall mean Licensor and any individual or Legal Entity
#       on behalf of whom a Contribution has been received by Licensor and
#       subsequently incorporated within the Work.
#
#    2. Grant of Copyright License. Subject to the terms and conditions of
#       this License, each Contributor hereby grants to You a perpetual,
#       worldwide, non-exclusive, no-charge, royalty-free, irrevocable
#       copyright license to reproduce, prepare Derivative Works of,
#       publicly display, publicly perform, sublicense, and distribute the
#       Work and such Derivative Works in Source or Object form.
#
#    3. Grant of Patent License. Subject to the terms and conditions of
#       this License, each Contributor hereby grants to You a perpetual,
#       worldwide, non-exclusive, no-charge, royalty-free, irrevocable
#       (except as stated in this section) patent license to make, have made,
#       use, offer to sell, sell, import, and otherwise transfer the Work,
#       where such license applies only to those patent claims licensable
#       by such Contributor that are necessarily infringed by their
#       Contribution(s) alone or by combination of their Contribution(s)
#       with the Work to which such Contribution(s) was submitted. If You
#       institute patent litigation against any entity (including a
#       cross-claim or counterclaim in a lawsuit) alleging that the Work
#       or a Contribution incorporated within the Work constitutes direct
#       or contributory patent infringement, then any patent licenses
#       granted to You under this License for that Work shall terminate
#       as of the date such litigation is filed.
#
#    4. Redistribution. You may reproduce and distribute copies of the
#       Work or Derivative Works thereof in any medium, with or without
#       modifications, and in Source or Object form, provided that You
#       meet the following conditions:
#
#       (a) You must give any other recipients of the Work or
#           Derivative Works a copy of this License; and
#
#       (b) You must cause any modified files to carry prominent notices
#           stating that You changed the files; and
#
#       (c) You must retain, in the Source form of any Derivative Works
#           that You distribute, all copyright, patent, trademark, and
#           attribution notices from the Source form of the Work,
#           excluding those notices that do not pertain to any part of
#           the Derivative Works; and
#
#       (d) If the Work includes a "NOTICE" text file as part of its
#           distribution, then any Derivative Works that You distribute must
#           include a readable copy of the attribution notices contained
#           within such NOTICE file, excluding those notices that do not
#           pertain to any part of the Derivative Works, in at least one
#           of the following places: within a NOTICE text file distributed
#           as part of the Derivative Works; within the Source form or
#           documentation, if provided along with the Derivative Works; or,
#           within a display generated by the Derivative Works, if and
#           wherever such third-party notices normally appear. The contents
#           of the NOTICE file are for informational purposes only and
#           do not modify the License. You may add Your own attribution
#           notices within Derivative Works that You distribute, alongside
#           or as an addendum to the NOTICE text from the Work, provided
#           that such additional attribution notices cannot be construed
#           as modifying the License.
#
#       You may add Your own copyright statement to Your modifications and
#       may provide additional or different license terms and conditions
#       for use, reproduction, or distribution of Your modifications, or
#       for any such Derivative Works as a whole, provided Your use,
#       reproduction, and distribution of the Work otherwise complies with
#       the conditions stated in this License.
#
#    5. Submission of Contributions. Unless You explicitly state otherwise,
#       any Contribution intentionally submitted for inclusion in the Work
#       by You to the Licensor shall be under the terms and conditions of
#       this License, without any additional terms or conditions.
#       Notwithstanding the above, nothing herein shall supersede or modify
#       the terms of any separate license agreement you may have executed
#       with Licensor regarding such Contributions.
#
#    6. Trademarks. This License does not grant permission to use the trade
#       names, trademarks, service marks, or product names of the Licensor,
#       except as required for reasonable and customary use in describing the
#       origin of the Work and reproducing the content of the NOTICE file.
#
#    7. Disclaimer of Warranty. Unless required by applicable law or
#       agreed to in writing, Licensor provides the Work (and each
#       Contributor provides its Contributions) on an "AS IS" BASIS,
#       WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
#       implied, including, without limitation, any warranties or conditions
#       of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
#       PARTICULAR PURPOSE. You are solely responsible for determining the
#       appropriateness of using or redistributing the Work and assume any
#       risks associated with Your exercise of permissions under this License.
#
#    8. Limitation of Liability. In no event and under no legal theory,
#       whether in tort (including negligence), contract, or otherwise,
#       unless required by applicable law (such as deliberate and grossly
#       negligent acts) or agreed to in writing, shall any Contributor be
#       liable to You for damages, including any direct, indirect, special,
#       incidental, or consequential damages of any character arising as a
#       result of this License or out of the use or inability to use the
#       Work (including but not limited to damages for loss of goodwill,
#       work stoppage, computer failure or malfunction, or any and all
#       other commercial damages or losses), even if such Contributor
#       has been advised of the possibility of such damages.
#
#    9. Accepting Warranty or Additional Liability. While redistributing
#       the Work or Derivative Works thereof, You may choose to offer,
#       and charge a fee for, acceptance of support, warranty, indemnity,
#       or other liability obligations and/or rights consistent with this
#       License. However, in accepting such obligations, You may act only
#       on Your own behalf and on Your sole responsibility, not on behalf
#       of any other Contributor, and only if You agree to indemnify,
#       defend, and hold each Contributor harmless for any liability
#       incurred by, or claims asserted against, such Contributor by reason
#       of your accepting any such warranty or additional liability.
#
#    END OF TERMS AND CONDITIONS
#
#    APPENDIX: How to apply the Apache License to your work.
#
#       To apply the Apache License to your work, attach the following
#       boilerplate notice, with the fields enclosed by brackets "[]"
#       replaced with your own identifying information. (Don't include
#       the brackets!)  The text should be enclosed in the appropriate
#       comment syntax for the file format. We also recommend that a
#       file or class name and description of purpose be included on the
#       same "printed page" as the copyright notice for easier
#       identification within third-party archives.
#
#    Copyright 2022 Fraunhofer AISEC
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import os
import signal
import sys
import logging
import subprocess
import argparse

from abc import ABC, abstractmethod

LOG = "testbed-setup.log"
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG),
    ],
)


class AbstractInstaller(ABC):

    def __init__(self, sudo_consent: bool = True):
        self.counter = 1
        self.sudo_consent = sudo_consent

    def install_dependencies(self) -> None:
        self.execute_installation_step("OpenSSL", callback=self.install_openssl)
        self.execute_installation_step("Docker", callback=self.install_docker)
        self.create_certificates()

    # shared functions
    def execute_command(self, command: str, shell_mode: bool) -> None:
        requires_root = "sudo" in command
        if self.sudo_consent \
                and requires_root or "sudo" in command \
                and input(f"Run sudo command?:\n# {command}\n(YES/no)\n").lower() not in ["", "y", "yes"]:
            logging.debug("Exiting, due to lacking agreement to run with sudo.")
            sys.exit(1)

        logging.debug(command)
        # Running command with shell-like syntax requires a string and not a list of tokens.
        command = command if shell_mode else command.split(" ")
        print(f"Running command {command}")
        try:
            subprocess.run(command, shell=shell_mode) \
                .check_returncode()
        except subprocess.CalledProcessError as e:
            logging.critical(f"Previous command failed with {e}")
            print(f"Command failed, check logfile at {LOG}", file=sys.stderr)
            AbstractInstaller.abort()

    def log_step(self, description: str):
        print(f"{'=' * 6} {self.counter}. {description} {'=' * 6}")
        self.counter += 1

    def execute_installation_step(self, description: str, callback):
        self.log_step(f"{description} installation")
        answer = input(f"Do you want to install {description}? (YES/no)\n") \
            .lower()
        if answer in ["", "y", "yes"]:
            callback()
        elif answer == "skip":
            print(f"Skipping {description} installation.")
        else:
            AbstractInstaller.abort()

    def create_certificates(self) -> None:
        self.log_step(f"Creating testbed internal certificates.")
        command = "./create-certs.sh"
        try:
            subprocess.run(command.split(" "), cwd="certificates") \
                .check_returncode()
        except subprocess.CalledProcessError as e:
            logging.fatal(f"Failed to create certificates, with error: {e}.")
            self.abort()

    @staticmethod
    def abort():
        logging.fatal(f"Installation failed, check logfile at {LOG}")
        sys.exit(-1)

    # required steps
    @abstractmethod
    def update_package_manager(self) -> None:
        pass

    @abstractmethod
    def install_openssl(self) -> None:
        pass

    @abstractmethod
    def install_docker(self) -> None:
        pass

    @abstractmethod
    def install_apache2utils(self) -> None:
        pass


class DebianInstaller(AbstractInstaller):
    def install_apache2utils(self) -> None:
        self.execute_command("sudo apt-get install apache2-utils", shell_mode=False)

    def update_package_manager(self) -> None:
        self.execute_command("sudo apt-get update", shell_mode=False)

    def install_openssl(self) -> None:
        self.execute_command("sudo apt-get install -y openssl", shell_mode=False)

    def install_docker(self) -> None:
        logging.debug(f"Installing Docker according to https://docs.docker.com/engine/install/debian/")

        if input(
                "Do you want to uninstall potentially existing old Docker versions?"
                "Explanation available at: https://docs.docker.com/engine/install/debian/#uninstall-old-versions\n"
                "(YES/no)\n"
        ).lower() in ["n", "no"]:
            logging.debug("Uninstalling old docker versions.")
            self.execute_command("apt-get remove docker docker-engine docker.io containerd runc", shell_mode=False)

        logging.debug("Installing dependencies for Docker.")
        self.execute_command(
            command="sudo apt-get install ca-certificates curl gnupg lsb-release",
            shell_mode=False
        )

        logging.debug("Add Docker’s official GPG key.")
        self.execute_command("sudo mkdir -p /etc/apt/keyrings", shell_mode=False)
        self.execute_command(
            command="curl -fsSL https://download.docker.com/linux/debian/gpg"
                    " | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg",  # Note, sudo above is handled by function.
            shell_mode=True,
        )

        logging.debug("Setting up official docker repository.")
        self.execute_command(
            command="echo"
                    " \"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian"
                    " $(lsb_release -cs) stable\""
                    " | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null",
            shell_mode=True,
        )
        logging.debug("Installing the Docker Engine.")
        self.execute_command("sudo apt-get update", shell_mode=False)
        self.execute_command("sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin",
                             shell_mode=False)


class UbuntuInstaller(DebianInstaller):
    def install_docker(self) -> None:
        logging.debug(f"Installing Docker according to https://docs.docker.com/engine/install/ubuntu/")

        if input(
                "Do you want to uninstall potentially existing old Docker versions?"
                "Explanation available at: https://docs.docker.com/engine/install/ubuntu/#uninstall-old-versions\n"
                "(YES/no)\n"
        ).lower() in ["n", "no"]:
            logging.debug("Uninstalling old docker versions.")
            self.execute_command("apt-get remove docker docker-engine docker.io containerd runc", shell_mode=False)

        logging.debug("Installing dependencies for Docker.")
        self.execute_command(
            command="sudo apt-get install ca-certificates curl gnupg lsb-release",
            shell_mode=False,
        )

        logging.debug("Add Docker’s official GPG key.")
        self.execute_command("sudo mkdir -p /etc/apt/keyrings", shell_mode=False)
        self.execute_command(
            command="curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg",
            shell_mode=True,
        )

        logging.debug("Setting up official docker repository.")
        self.execute_command(
            command="echo"
                    " \"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu"
                    " $(lsb_release -cs) stable\""
                    " | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null",
            shell_mode=True,
        )
        logging.debug("Installing the Docker Engine.")
        self.execute_command("sudo apt-get update", shell_mode=False)
        self.execute_command(command="sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin",
                             shell_mode=False)


class ArchInstaller(AbstractInstaller):

    def install_apache2utils(self) -> None:
        self.execute_command("sudo pacman -S apache", shell_mode=False)

    def update_package_manager(self) -> None:
        self.execute_command("sudo pacman -Sy", shell_mode=False)

    def install_openssl(self) -> None:
        logging.debug("OpenSSL is installed by default on Arch, nothing to do.")

    def install_docker(self) -> None:
        self.execute_command("sudo pacman -Sy docker docker-compose", shell_mode=False)


def main():
    parser = argparse.ArgumentParser("plc-testbed helper.")
    parser.add_argument(
        "--install",
        type=str,
        nargs=1,
        choices=[
            "debian",
            "ubuntu",
            "arch",
        ],
        dest="install",
    )
    parser.add_argument(
        "--start",
        type=str,
        nargs=1,
        choices=[
            "prod",
            "local",
            "dev",
        ],
        dest="start",
    )

    parser.add_argument(
        "--build",
        type=str,
        nargs=1,
        choices=[
            "prod",
            "local",
            "dev",
        ],
        dest="build",
    )
    parser.add_argument(
        "--stop",
        action="store_true",
        dest="stop",
    )
    parser.add_argument(
        "--dont-ask-sudo",
        action="store_false",
        dest="sudo_consent",
    )

    args = parser.parse_args()

    if args.install and "debian" in args.install:
        logging.debug("Running Debian installer.")
        DebianInstaller(sudo_consent=args.sudo_consent).install_dependencies()
    elif args.install and "ubuntu" in args.install:
        logging.debug("Running Ubuntu installer.")
        UbuntuInstaller(sudo_consent=args.sudo_consent).install_dependencies()
    elif args.install and "arch" in args.install:
        logging.debug("Running Arch installer.")
        ArchInstaller(sudo_consent=args.sudo_consent).install_dependencies()

    if args.build is not None:
        command = f"sudo docker compose -f docker-compose.yml -f docker-compose.{args.build[0]}.yml build"
        print(f"Building dev version of testbed...\n$ {command}")
        try:
            subprocess.run(command.split(" ")).check_returncode()
        except subprocess.CalledProcessError as e:
            print(f"Failed to start testbed, error is: {e}")
            exit(1)

    if args.start is not None:
        if "prod" in args.start and not os.path.exists("nginx/dhparam.pem"):
            print("Generating DH parameters.")
            try:
                subprocess.run("openssl dhparam -out nginx/dhparam.pem 2048").check_returncode()
            except subprocess.CalledProcessError as e:
                print(f"Failed to create dhparams.pem with error: {e}")
                exit(1)
        version = args.start[0]
        command = f"sudo docker compose -f docker-compose.yml -f docker-compose.{version}.yml up -d"
        print(f"Starting {version} version of testbed...\n$ {command}")
        try:
            with open(".currently-running", "w+") as f:
                f.write(f"{version}")
            subprocess.run(command.split(" ")).check_returncode()
        except subprocess.CalledProcessError as e:
            print(f"Failed to start testbed, with error {e}.", file=sys.stderr)
            exit(1)

    if args.stop:
        with open(".currently-running") as f:
            version = f.read().rstrip()
        print("Stopping testbed...")
        command = f"sudo docker compose -f docker-compose.yml -f docker-compose.{version}.yml down"
        try:
            subprocess.run(command.split(" ")).check_returncode()
            print("Testbed has stopped.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to stop testbed with error {e}", file=sys.stderr)
            exit(1)


if __name__ == "__main__":
    main()
