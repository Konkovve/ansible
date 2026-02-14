#!/usr/bin/python3
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule

def main():
    # Описываем входные аргументы
    module = AnsibleModule(
        argument_spec=dict(
            target_port=dict(type='int', required=True)
        )
    )

    port = module.params['target_port']

    if port < 1 or port > 65535:
        module.fail_json(msg=f"Port {port} is invalid! Must be 1-65535")

    module.exit_json(
        changed=False, 
        validated_port=port, 
        msg="Port is valid"
    )

if __name__ == '__main__':
    main()