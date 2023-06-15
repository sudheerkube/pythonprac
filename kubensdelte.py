from kubernetes import client, watch

def finalize(deployment, namespace, finalizer):
    print(f"Do some pre-deletion task related to the {finalizer} present in {namespace}/{deployment}")
    ...

v1 = client.AppsV1Api(api_client)
w = watch.Watch()
for deploy in w.stream(partial(v1.list_namespaced_deployment, namespace=ns)):
    print(f"Deploy - Message: Event type: {deploy['type']}, Deployment {deploy['object']['metadata']['name']} was changed.")
    if deploy['type'] == "MODIFIED" and "deletionTimestamp" in deploy['object']['metadata']:

        fins = deploy['object']['metadata']['finalizers']
        f = fins[0]
        finalize(deploy['object']['metadata']['name'], ns, f)
        new_fins = list(set(fins) - {f})
        body = [{
            "kind": "Deployment",
            "apiVersion": "apps/v1",
            "metadata": {
                "name": deploy['object']['metadata']['name'],
            },
            "op": "replace",
            "path": f"/metadata/finalizers",
            "value": new_fins
        }]
        resp = v1.patch_namespaced_deployment(name=deploy['object']['metadata']['name'],
                                              namespace=ns,
                                              body=body,
                                              field_manager="json")
    elif deploy['type'] == "DELETED":
        print(f"{deploy['object']['metadata']['name']} successfully deleted.")
print("Finished namespace stream.")x