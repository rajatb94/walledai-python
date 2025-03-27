# Changelog

## 0.16.0-alpha (2025-03-27)

Full Changelog: [v0.15.0-alpha...v0.16.0-alpha](https://github.com/rajatb94/walledai-python/compare/v0.15.0-alpha...v0.16.0-alpha)

### Features

* **client:** allow passing `NotGiven` for body ([#60](https://github.com/rajatb94/walledai-python/issues/60)) ([732bebf](https://github.com/rajatb94/walledai-python/commit/732bebfea9bffe1770fb5a306af76d40f1147f70))
* **client:** send `X-Stainless-Read-Timeout` header ([#55](https://github.com/rajatb94/walledai-python/issues/55)) ([941f911](https://github.com/rajatb94/walledai-python/commit/941f9110e97a78c01ce7bfb236a4022457ddab7e))


### Bug Fixes

* asyncify on non-asyncio runtimes ([#59](https://github.com/rajatb94/walledai-python/issues/59)) ([0473ddf](https://github.com/rajatb94/walledai-python/commit/0473ddf52b53e056a222aea15e93a17efaaae2d3))
* **ci:** ensure pip is always available ([#71](https://github.com/rajatb94/walledai-python/issues/71)) ([607209d](https://github.com/rajatb94/walledai-python/commit/607209d74900439451d8700565a4a2e94cffaee2))
* **ci:** remove publishing patch ([#72](https://github.com/rajatb94/walledai-python/issues/72)) ([e762b2e](https://github.com/rajatb94/walledai-python/commit/e762b2e1f527464d4d315ba4bcb3b1f405600b93))
* **client:** mark some request bodies as optional ([732bebf](https://github.com/rajatb94/walledai-python/commit/732bebfea9bffe1770fb5a306af76d40f1147f70))
* **types:** handle more discriminated union shapes ([#70](https://github.com/rajatb94/walledai-python/issues/70)) ([e70577b](https://github.com/rajatb94/walledai-python/commit/e70577bfebc80480f0dd2bcaef96270990a45374))


### Chores

* **docs:** update client docstring ([#64](https://github.com/rajatb94/walledai-python/issues/64)) ([06185b8](https://github.com/rajatb94/walledai-python/commit/06185b84ccc0ee014815c3de3eecb2441cb5032b))
* fix typos ([#73](https://github.com/rajatb94/walledai-python/issues/73)) ([9587711](https://github.com/rajatb94/walledai-python/commit/958771153c0a36f381148234fb41550b17b46103))
* **internal:** bummp ruff dependency ([#54](https://github.com/rajatb94/walledai-python/issues/54)) ([293daba](https://github.com/rajatb94/walledai-python/commit/293dabae13c60421d1f70ecfffabb82e5ec30e5e))
* **internal:** bump rye to 0.44.0 ([#69](https://github.com/rajatb94/walledai-python/issues/69)) ([1321d05](https://github.com/rajatb94/walledai-python/commit/1321d054e2bd5d81ee8ff728cb5501936241ed26))
* **internal:** change default timeout to an int ([#52](https://github.com/rajatb94/walledai-python/issues/52)) ([e9caaf0](https://github.com/rajatb94/walledai-python/commit/e9caaf0ae6211f81bc77615b93070e610c141931))
* **internal:** codegen related update ([#68](https://github.com/rajatb94/walledai-python/issues/68)) ([65f61c9](https://github.com/rajatb94/walledai-python/commit/65f61c9792c46a85d2b764247b4139993ff75693))
* **internal:** fix devcontainers setup ([#61](https://github.com/rajatb94/walledai-python/issues/61)) ([86baf71](https://github.com/rajatb94/walledai-python/commit/86baf71ea8cd1daf2e8a05c39fd5c37efa7642e8))
* **internal:** fix type traversing dictionary params ([#56](https://github.com/rajatb94/walledai-python/issues/56)) ([e2966b8](https://github.com/rajatb94/walledai-python/commit/e2966b8d32839d2ace23d562be36f91b981132de))
* **internal:** minor type handling changes ([#57](https://github.com/rajatb94/walledai-python/issues/57)) ([246bdf6](https://github.com/rajatb94/walledai-python/commit/246bdf60c55cb9e26b36b99f0ea5198ff90554f0))
* **internal:** properly set __pydantic_private__ ([#62](https://github.com/rajatb94/walledai-python/issues/62)) ([a7e476e](https://github.com/rajatb94/walledai-python/commit/a7e476ead0dbdd3b639766fee00a1c5dc683e4da))
* **internal:** remove extra empty newlines ([#67](https://github.com/rajatb94/walledai-python/issues/67)) ([85bc4cd](https://github.com/rajatb94/walledai-python/commit/85bc4cdf819a8ced971fa0ff9b12edbb74c12053))
* **internal:** remove unused http client options forwarding ([#65](https://github.com/rajatb94/walledai-python/issues/65)) ([ba646f9](https://github.com/rajatb94/walledai-python/commit/ba646f9a958ad0767ee547e38da8d36a633623b3))
* **internal:** update client tests ([#58](https://github.com/rajatb94/walledai-python/issues/58)) ([912479f](https://github.com/rajatb94/walledai-python/commit/912479fb88e040f1dcd7b9acbcb51b6d7eb7b738))


### Documentation

* update URLs from stainlessapi.com to stainless.com ([#63](https://github.com/rajatb94/walledai-python/issues/63)) ([c086085](https://github.com/rajatb94/walledai-python/commit/c0860850fa8f33cfefc5a76ace776b9e2ecd8989))

## 0.15.0-alpha (2025-01-24)

Full Changelog: [v0.14.0-alpha...v0.15.0-alpha](https://github.com/rajatb94/walledai-python/compare/v0.14.0-alpha...v0.15.0-alpha)

### Features

* **api:** update via SDK Studio ([#49](https://github.com/rajatb94/walledai-python/issues/49)) ([d3d3fcd](https://github.com/rajatb94/walledai-python/commit/d3d3fcd85ac4d205437d590469614f40949fe158))

## 0.14.0-alpha (2024-05-15)

Full Changelog: [v0.13.0-alpha...v0.14.0-alpha](https://github.com/rajatb94/walledai-python/compare/v0.13.0-alpha...v0.14.0-alpha)

### Features

* **api:** update via SDK Studio ([#46](https://github.com/rajatb94/walledai-python/issues/46)) ([c9de5bf](https://github.com/rajatb94/walledai-python/commit/c9de5bfcd6001019ed8b8e4acef14cecbc851124))

## 0.13.0-alpha (2024-05-15)

Full Changelog: [v0.12.0-alpha...v0.13.0-alpha](https://github.com/rajatb94/walledai-python/compare/v0.12.0-alpha...v0.13.0-alpha)

### Features

* **api:** update via SDK Studio ([#42](https://github.com/rajatb94/walledai-python/issues/42)) ([8462b94](https://github.com/rajatb94/walledai-python/commit/8462b944d423ef2dadcf17891219784ef735dc50))
* **api:** update via SDK Studio ([#44](https://github.com/rajatb94/walledai-python/issues/44)) ([4e3235b](https://github.com/rajatb94/walledai-python/commit/4e3235bd3db5a40adf9898c2d7bcc3a166609164))

## 0.12.0-alpha (2024-05-15)

Full Changelog: [v0.11.0-alpha...v0.12.0-alpha](https://github.com/rajatb94/walledai-python/compare/v0.11.0-alpha...v0.12.0-alpha)

### Features

* **api:** update via SDK Studio ([#39](https://github.com/rajatb94/walledai-python/issues/39)) ([8c5dac2](https://github.com/rajatb94/walledai-python/commit/8c5dac2ef7597eb403038fb6024c84cb50c840a3))

## 0.11.0-alpha (2024-05-15)

Full Changelog: [v0.10.0-alpha...v0.11.0-alpha](https://github.com/rajatb94/walledai-python/compare/v0.10.0-alpha...v0.11.0-alpha)

### Features

* **api:** update via SDK Studio ([#36](https://github.com/rajatb94/walledai-python/issues/36)) ([21b3bd0](https://github.com/rajatb94/walledai-python/commit/21b3bd01e2ed4db1713578a523a6828d352df441))

## 0.10.0-alpha (2024-05-15)

Full Changelog: [v0.9.0-alpha...v0.10.0-alpha](https://github.com/rajatb94/walledai-python/compare/v0.9.0-alpha...v0.10.0-alpha)

### Features

* **api:** update via SDK Studio ([#33](https://github.com/rajatb94/walledai-python/issues/33)) ([ff8031d](https://github.com/rajatb94/walledai-python/commit/ff8031dba7a2ebdffe89eb786b56bb63379c1ecd))

## 0.9.0-alpha (2024-05-15)

Full Changelog: [v0.8.0-alpha...v0.9.0-alpha](https://github.com/rajatb94/walledai-python/compare/v0.8.0-alpha...v0.9.0-alpha)

### Features

* **api:** update via SDK Studio ([#30](https://github.com/rajatb94/walledai-python/issues/30)) ([f5390d7](https://github.com/rajatb94/walledai-python/commit/f5390d73a207ddd8adb6d9194712e49f1fd3ce5e))

## 0.8.0-alpha (2024-05-15)

Full Changelog: [v0.7.0-alpha...v0.8.0-alpha](https://github.com/rajatb94/walledai-python/compare/v0.7.0-alpha...v0.8.0-alpha)

### Features

* **api:** update via SDK Studio ([#27](https://github.com/rajatb94/walledai-python/issues/27)) ([725419a](https://github.com/rajatb94/walledai-python/commit/725419ae30876523709a6ad1cade2b9c07fd6d9d))

## 0.7.0-alpha (2024-05-14)

Full Changelog: [v0.6.0-alpha...v0.7.0-alpha](https://github.com/rajatb94/walledai-python/compare/v0.6.0-alpha...v0.7.0-alpha)

### Features

* **api:** update via SDK Studio ([#24](https://github.com/rajatb94/walledai-python/issues/24)) ([a0d5993](https://github.com/rajatb94/walledai-python/commit/a0d5993d77e9e9753f2c52e53c73da1613303602))

## 0.6.0-alpha (2024-05-14)

Full Changelog: [v0.5.0-alpha...v0.6.0-alpha](https://github.com/rajatb94/walledai-python/compare/v0.5.0-alpha...v0.6.0-alpha)

### Features

* **api:** update via SDK Studio ([#20](https://github.com/rajatb94/walledai-python/issues/20)) ([7c61ec4](https://github.com/rajatb94/walledai-python/commit/7c61ec455aa353e983342c98a4b1878625abfd1c))
* **api:** update via SDK Studio ([#22](https://github.com/rajatb94/walledai-python/issues/22)) ([90da5a1](https://github.com/rajatb94/walledai-python/commit/90da5a15e301a12fd8fd9ca2f01afdcae7fa4c9f))

## 0.5.0-alpha (2024-05-14)

Full Changelog: [v0.4.0-alpha...v0.5.0-alpha](https://github.com/rajatb94/walledai-python/compare/v0.4.0-alpha...v0.5.0-alpha)

### Features

* **api:** update via SDK Studio ([bb9e474](https://github.com/rajatb94/walledai-python/commit/bb9e4742269966e767fa455831bb645090ead925))
* **api:** update via SDK Studio ([#16](https://github.com/rajatb94/walledai-python/issues/16)) ([1b75418](https://github.com/rajatb94/walledai-python/commit/1b75418b401ed9e85a240a951cfe48cd27fa930e))
* **api:** update via SDK Studio ([#18](https://github.com/rajatb94/walledai-python/issues/18)) ([56717ce](https://github.com/rajatb94/walledai-python/commit/56717cea3d8bc80e3582a0c6e441af09d761967e))

## 0.4.0-alpha (2024-05-14)

Full Changelog: [v0.3.0-alpha...v0.4.0-alpha](https://github.com/rajatb94/walledai-python/compare/v0.3.0-alpha...v0.4.0-alpha)

### Features

* **api:** update via SDK Studio ([#13](https://github.com/rajatb94/walledai-python/issues/13)) ([6e15919](https://github.com/rajatb94/walledai-python/commit/6e15919ad8ba5c0a52a0deeacc4b4aeec453aef2))

## 0.3.0-alpha (2024-05-14)

Full Changelog: [v0.2.0-alpha...v0.3.0-alpha](https://github.com/rajatb94/walledai-python/compare/v0.2.0-alpha...v0.3.0-alpha)

### Features

* **api:** update via SDK Studio ([#11](https://github.com/rajatb94/walledai-python/issues/11)) ([fb7e370](https://github.com/rajatb94/walledai-python/commit/fb7e3704cb5b08f6bd51ef3c714f9cb13c8949e7))
* **api:** update via SDK Studio ([#9](https://github.com/rajatb94/walledai-python/issues/9)) ([571e707](https://github.com/rajatb94/walledai-python/commit/571e7070a8bbc21703478b8bb4485ebadaedd928))

## 0.2.0-alpha (2024-05-14)

Full Changelog: [v0.1.0-alpha...v0.2.0-alpha](https://github.com/rajatb94/walledai-python/compare/v0.1.0-alpha...v0.2.0-alpha)

### Features

* **api:** update via SDK Studio ([#6](https://github.com/rajatb94/walledai-python/issues/6)) ([6d21723](https://github.com/rajatb94/walledai-python/commit/6d217235ea9616c46c3c2ea3e6bba97ace2b24ad))

## 0.1.0-alpha (2024-05-13)

Full Changelog: [v0.0.1-alpha...v0.1.0-alpha](https://github.com/rajatb94/walledai-python/compare/v0.0.1-alpha...v0.1.0-alpha)

### Features

* **api:** update via SDK Studio ([#4](https://github.com/rajatb94/walledai-python/issues/4)) ([067d93e](https://github.com/rajatb94/walledai-python/commit/067d93e14b0b46e44bfde80a4a7fc0da374565bd))

## 0.0.1-alpha (2024-05-13)

Full Changelog: [v0.0.1-alpha.0...v0.0.1-alpha](https://github.com/rajatb94/walledai-python/compare/v0.0.1-alpha.0...v0.0.1-alpha)

### Features

* **api:** update via SDK Studio ([0db116f](https://github.com/rajatb94/walledai-python/commit/0db116f19d228a34ca1053189e17b717e85809ba))
* **api:** update via SDK Studio ([1f830e7](https://github.com/rajatb94/walledai-python/commit/1f830e71ac3b6091da444174838403a29f781908))


### Chores

* configure new SDK language ([4a873a4](https://github.com/rajatb94/walledai-python/commit/4a873a4bd7d50220647023266f713e0da34542ac))
* go live ([#1](https://github.com/rajatb94/walledai-python/issues/1)) ([7d01dd9](https://github.com/rajatb94/walledai-python/commit/7d01dd93665791b9361d6e3c89a89645eb772a83))
