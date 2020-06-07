def My_stage_2_task(data):
    return_string_info = "Hello World, this is {} with HNGi7 ID {} and email {} using {} for stage 2 task"
    return(return_string_info.format(data['name'], data['id'], data['email'], data['language']))


if __name__ == '__main__':

    details = {"name": "Njoku Genesis Victor",
               "id": "HNG-00522",
               "email": "genesisgreat93@outlook.com",
               "language": "python",
               }

    print(My_stage_2_task(details))
