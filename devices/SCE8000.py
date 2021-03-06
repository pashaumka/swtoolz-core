# coding=UTF8
# Строчка выше нужна на случай использования Non-ASCII символов, например кириллицы.

# Корректирующий множитель для таймаута SNMP-операций. Чем медленнее CPU устройства, тем больше должен быть множитель.
# Этот параметр используется (если задан) для swtoolz-core. Остальные параметры целиком определяются пользователем.
timeout_mf = 1.2

# Карта портов устройства. Представлена в виде списков слотов. Каждый слот содержит список рядов. Каждый ряд содержит список портов.
DeviceMap = ([
    [
	['1','2','3','4','5','6']
    ],
    ],)

# SlotSize - количество индексов, отведенное на слот. Обычно это 64, то есть слот №1 - 1..64, слот №2 - 65..128, слот №3 - 129..192 и так далее.
# ShiftIndex - смещение, которое нужно прибавить к индексу. У некоторых устройств первый индекс может начинаться, например, с 256.
# MaxIndex - Максимальный индекс, который нужно обработать. Индексы с большими номерами игнорируются.
StackInfo = ({
    'SlotSize'   : '8',
    'ShiftIndex' : '0',
    'MaxIndex'   : '12',
    },)

# Список рекомендуемых команд
Commands = ([
    'DeviceMap',
    'StackInfo',
    'MediumType',
    'ActualStatus',
    'ActualSpeed',
    'AdminStatus',
    'BoardDescr',
    'walk_PortIndex',
    'walk_ifName',
    'walk_ifAlias',
    ],)

# ifType
MediumType = ({
    '1' : 'other',
    '6' : 'copper',
    '24': 'loopback',
    '53': 'virtual',
    },)

# ifOperStatus
ActualStatus = ({
    '1' : 'linkup',
    '2' : 'linkdown',
    '3' : 'testing',
    '4' : 'unknown',
    '5' : 'dormant',
    '6' : 'notPresent',
    '7' : 'lowerLayerDown',
    },)

# ifHighSpeed
ActualSpeed = ({
    '0'    : 'linkdown',
    '10'   : '10M',
    '100'  : '100M',
    '1000' : '1G',
    '10000': '10G',
    },)

# ifAdminStatus
AdminStatus = ({
    '1' : 'enabled',
    '2' : 'disabled',
    '3' : 'testing',
    },)

# ifType (placeholder)
AdminSpeed = ({
    '1' : 'other',
    '6' : 'other',
    '24': 'other',
    '53': 'other',
    },)

# ifType (placeholder)
AdminFlow = ({
    '1' : 'disabled',
    '6' : 'disabled',
    '24': 'disabled',
    '53': 'disabled',
    },)

# UnitModuleName (placeholder)
BoardDescr = ({
    '1' : 'Cisco SCE8000',
    },)

# get_HardwareRev (placeholder for Slava's Hardcode. not working but necessary)
get_HardwareRev = ({
    '0' : 'n/a',
    },)

# walk_VlanEgressPorts (placeholder for Slava's Hardcode. not working but necessary)
walk_VlanEgressPorts = ({
    '0' : '',
    },)

walk_PortIndex = {
#    PortIndex           .1.3.6.1.2.1.2.2.1.1				ifIndex
    'PortIndex'       : '.1.3.6.1.2.1.2.2.1.1',
    }

get_SinglePort = {
#    MediumType          .1.3.6.1.2.1.2.2.1.3				ifType
    'MediumType.'     : '.1.3.6.1.2.1.2.2.1.3.%s',
#    ActualStatus        .1.3.6.1.2.1.2.2.1.8				ifOperStatus
    'ActualStatus.'   : '.1.3.6.1.2.1.2.2.1.8.%s',
#    ActualSpeed         .1.3.6.1.2.1.31.1.1.1.15			ifHighSpeed
#    'ActualSpeed.'    : '.1.3.6.1.2.1.31.1.1.1.15.%s',
#    AdminStatus         .1.3.6.1.2.1.2.2.1.7				ifAdminStatus
    'AdminStatus.'    : '.1.3.6.1.2.1.2.2.1.7.%s',
#    AdminSpeed          .1.3.6.1.2.1.2.2.1.3				ifType (placeholder)
#    'AdminSpeed.'     : '.1.3.6.1.2.1.2.2.1.3.%s',
#    AdminFlow           .1.3.6.1.2.1.2.2.1.3				ifType (placeholder)
#    'AdminFlow.'      : '.1.3.6.1.2.1.2.2.1.3.%s',
#    PortDescr           .1.3.6.1.2.1.31.1.1.1.18			ifAlias
    'PortDescr.'      : '.1.3.6.1.2.1.31.1.1.1.18.%s',
    }

walk_AllPorts = {
#    MediumType          .1.3.6.1.2.1.2.2.1.3				ifType
    'MediumType'      : '.1.3.6.1.2.1.2.2.1.3',
#    ActualStatus        .1.3.6.1.2.1.2.2.1.8				ifOperStatus
    'ActualStatus'    : '.1.3.6.1.2.1.2.2.1.8',
#    ActualSpeed         .1.3.6.1.2.1.31.1.1.1.15			ifHighSpeed
#    'ActualSpeed'     : '.1.3.6.1.2.1.31.1.1.1.15',
#    AdminStatus         .1.3.6.1.2.1.2.2.1.7				ifAdminStatus
    'AdminStatus'     : '.1.3.6.1.2.1.2.2.1.7',
#    AdminSpeed          .1.3.6.1.2.1.2.2.1.3				ifType (placeholder)
#    'AdminSpeed'      : '.1.3.6.1.2.1.2.2.1.3',
#    AdminFlow           .1.3.6.1.2.1.2.2.1.3				ifType (placeholder)
#    'AdminFlow'       : '.1.3.6.1.2.1.2.2.1.3',
    }

walk_ifName = {
#    PortName            .1.3.6.1.2.1.31.1.1.1.1			ifName
    'PortName'        : '.1.3.6.1.2.1.31.1.1.1.1',
    }

walk_ifAlias = {
#    PortDescr           .1.3.6.1.2.1.31.1.1.1.18			ifAlias
    'PortDescr'       : '.1.3.6.1.2.1.31.1.1.1.18',
    }
