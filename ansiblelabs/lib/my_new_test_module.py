#!/usr/bin/python

ANSIBLE_METADATA = {
        'metadata_version': '1.1',
        'status': ['preview'],
        'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: my_net_test_module

short_description: This is a sample module

description:
    - "This is my longer description explaining the module"

options:
    name:
        description:
            - This is the message to send to the sample module
        required: true
    new:
        description:
            - Control to demo if the result of this module is changed or not
        required: false

author:
    - Nick Bolyard
'''
EXAMPLES = '''
#Pass in a message
- name: Test with a message
  my_new_test_module:
    name: hello world
    new: true

#pass in a message and have changed true
- name: Test with a message and changed output
  my_new_test_module:
    name: hello world
    new: true

# fail the module
- name: Test failure of module
  my_new_test_module:
    name: fail me
'''

RETURN = '''
original_message:
    description: The original name param that was passed in
    type: str
message:
    description: The output message the same module generates
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
            name=dict(type='str', required=True),
            new=dict(type='bool', required=False, default=False)
    )
    # seed the result dict in the object
    # we primarily care about changed and state
    # change is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in the subsequent task
    result = dict(
            changed=False,
            original_message='',
            message=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
            argument_spec=module_args,
            supports_check_mode=True
    )
    # if the user is working with this module in only check mode we do not
    # want to make changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        return result

    # manipulate or modify the state as needed
    result['original_message'] = module.params['name']
    result['message'] = 'goodbye'

    # use whatever logic you need to determine whether or not this module
    # made any mods
    if module.params['new']:
        result['changed'] = True

    # lets try customizing this code
    # here we have a basic conditional
    # if our module received a value 'who you gonna call' for the parameter 'name'
    # the returned message will be "GHOSTBUSTERS"
    if module.params['name'] == 'who you gonna call':
        result['message'] = 'GHOSTBUSTERS'

    if module.params['name'] == 'potatoes' or 'POTATOES':
        result['message'] = 'boil em, mash em, stick em in a stew'

    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes failure, run
    # AnsibleModule.fail_json() to pass int he message and the result
    if module.params['name'] == 'fail me':
        module.fail_json(msg='You requested this to fail', **result)

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
