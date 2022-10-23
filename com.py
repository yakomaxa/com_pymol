def com(target="all"):
    objs=cmd.get_object_list(target)
    com0=cmd.centerofmass(objs[-1])
    for obj in objs:
        com=cmd.centerofmass(obj)
        dcom=list()
        for i in range(0,3):
            dcom.append(com[i]-com0[i])
        cmd.translate([-x for x in dcom],obj,camera=0)


pymol.cmd.extend("com", com)
cmd.auto_arg[0]['com'] = cmd.auto_arg[0]['hide']
