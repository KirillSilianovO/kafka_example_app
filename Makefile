include .env
export

BUILDER_NAME = multi-arch-builder
ACTION = --load
ARCH=linux/amd64

.recreate_builder:
	docker buildx rm $(BUILDER_NAME) || true ; \
	export DOCKER_CLI_EXPERIMENTAL=enabled; \
	docker buildx create --use --name $(BUILDER_NAME)

.build: .recreate_builder
	docker buildx build \
		--platform=$(ARCH) \
		-t $(IMAGE_NAMESPACE)/$(IMAGE_NAME):$(VER) \
		-t $(IMAGE_NAMESPACE)/$(IMAGE_NAME):latest \
		-f $(SERVICE_DIR)/Dockerfile \
		$(SERVICE_DIR) \
		$(ACTION)

build_consumer: .recreate_builder
	$(MAKE) .build IMAGE_NAME=$(CONSUMER_IMAGE_NAME) SERVICE_DIR=$(PWD)/consumer

build_producer: .recreate_builder
	$(MAKE) .build IMAGE_NAME=$(PRODUCER_IMAGE_NAME) SERVICE_DIR=$(PWD)/producer

push_producer: .recreate_builder
	$(MAKE) .build IMAGE_NAME=$(PRODUCER_IMAGE_NAME) SERVICE_DIR=$(PWD)/producer ACTION=--push ARCH=linux/amd64,linux/arm64

push_consumer: .recreate_builder
	$(MAKE) .build IMAGE_NAME=$(PRODUCER_IMAGE_NAME) SERVICE_DIR=$(PWD)/producer ACTION=--push ARCH=linux/amd64,linux/arm64

build_all: build_producer build_consumer

push_all: push_producer push_consumer