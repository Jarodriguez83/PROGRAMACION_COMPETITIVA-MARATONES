# ==============================================
# OSCILOSCOPIO OPTICA Y LABORATORIO 
# ==============================================

import sys
import numpy as np
import pyqtgraph as pg

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QDial,
    QLineEdit
)

from PyQt5.QtCore import QTimer
from pyqtgraph import InfiniteLine


class Osciloscopio(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Osciloscopio Virtual")
        self.resize(1300, 750)

        # ==========================================
        # VARIABLES
        # ==========================================

        self.frecuencia = 5
        self.amplitud = 1

        self.generadorON = False

        self.tiempo = 0

        self.pausado = False
        self.cursorActivo = False

        self.xMin = 0
        self.xMax = 1

        # ==========================================
        # LAYOUT PRINCIPAL
        # ==========================================

        mainLayout = QHBoxLayout()

        # ==========================================
        # LADO IZQUIERDO
        # ==========================================

        ladoIzquierdo = QVBoxLayout()

        # ==========================================
        # PLOT OSCILOSCOPIO
        # ==========================================

        self.plotWidget = pg.PlotWidget()

        self.plotWidget.setBackground((10,10,10))

        self.plotWidget.showGrid(
            x=True,
            y=True
        )

        self.plotWidget.setYRange(-5, 5)

        self.plotWidget.setXRange(
            self.xMin,
            self.xMax
        )

        self.plotWidget.setLimits(
            xMin=self.xMin,
            xMax=self.xMax
        )

        # ==========================================
        # EJES
        # ==========================================

        self.plotWidget.getAxis('left').setPen(
            pg.mkPen((180,180,180))
        )

        self.plotWidget.getAxis('bottom').setPen(
            pg.mkPen((180,180,180))
        )

        # ==========================================
        # NOMBRES EJES
        # ==========================================

        self.plotWidget.setLabel(
            'left',
            'Voltaje',
            color='white',
            size='14pt'
        )

        self.plotWidget.setLabel(
            'bottom',
            'Tiempo',
            color='white',
            size='14pt'
        )

        # ==========================================
        # LINEA CENTRAL
        # ==========================================

        self.lineaCentral = InfiniteLine(
            pos=0,
            angle=0,
            movable=False,
            pen=pg.mkPen(
                color=(255,255,255),
                width=2
            )
        )

        self.plotWidget.addItem(
            self.lineaCentral
        )

        # ==========================================
        # CURVA
        # ==========================================

        self.curva = self.plotWidget.plot(
            pen=pg.mkPen(
                color=(255,255,0),
                width=2
            )
        )

        # ==========================================
        # CURSOR VERTICAL
        # ==========================================

        self.cursorV = InfiniteLine(
            pos=0,
            angle=90,
            movable=False,
            pen=pg.mkPen(
                color=(0,255,255),
                width=2
            )
        )

        self.cursorV.hide()

        self.plotWidget.addItem(
            self.cursorV
        )

        # ==========================================
        # CURSOR HORIZONTAL
        # ==========================================

        self.cursorH = InfiniteLine(
            pos=0,
            angle=0,
            movable=False,
            pen=pg.mkPen(
                color=(0,255,255),
                width=2
            )
        )

        self.cursorH.hide()

        self.plotWidget.addItem(
            self.cursorH
        )

        # ==========================================
        # CLICK MOUSE
        # ==========================================

        self.plotWidget.scene().sigMouseClicked.connect(
            self.mouseClicked
        )

        # ==========================================
        # AÑADIR PLOT
        # ==========================================

        ladoIzquierdo.addWidget(
            self.plotWidget
        )

        # ==========================================
        # GENERADOR
        # ==========================================

        generadorLayout = QVBoxLayout()

        tituloGen = QLabel(
            "GENERADOR DE SEÑAL"
        )

        tituloGen.setStyleSheet("""
            color: black;
            background-color: lightgray;
            font-size: 20px;
            font-weight: bold;
            padding: 10px;
        """)

        generadorLayout.addWidget(
            tituloGen
        )

        # ==========================================
        # BOTON GENERADOR
        # ==========================================

        self.botonGenerador = QPushButton(
            "GENERADOR: OFF"
        )

        self.botonGenerador.setStyleSheet("""
            QPushButton{
                background-color: red;
                color: white;
                font-size: 16px;
                border-radius: 10px;
                padding: 10px;
            }
        """)

        self.botonGenerador.clicked.connect(
            self.toggleGenerador
        )

        generadorLayout.addWidget(
            self.botonGenerador
        )

        # ==========================================
        # FRECUENCIA
        # ==========================================

        textoFreq = QLabel(
            "Frecuencia (Hz)"
        )

        textoFreq.setStyleSheet("""
            color: black;
            font-size: 16px;
            font-weight: bold;
        """)

        generadorLayout.addWidget(
            textoFreq
        )

        self.inputFreq = QLineEdit()

        self.inputFreq.setText("5")

        self.inputFreq.setStyleSheet("""
            background-color: white;
            color: black;
            font-size: 16px;
            padding: 5px;
        """)

        self.inputFreq.editingFinished.connect(
            self.actualizarFrecuencia
        )

        generadorLayout.addWidget(
            self.inputFreq
        )

        # ==========================================
        # AMPLITUD
        # ==========================================

        textoAmp = QLabel(
            "Voltaje / Amplitud (V)"
        )

        textoAmp.setStyleSheet("""
            color: black;
            font-size: 16px;
            font-weight: bold;
        """)

        generadorLayout.addWidget(
            textoAmp
        )

        self.inputAmp = QLineEdit()

        self.inputAmp.setText("1")

        self.inputAmp.setStyleSheet("""
            background-color: white;
            color: black;
            font-size: 16px;
            padding: 5px;
        """)

        self.inputAmp.editingFinished.connect(
            self.actualizarAmplitud
        )

        generadorLayout.addWidget(
            self.inputAmp
        )

        # ==========================================
        # AÑADIR GENERADOR
        # ==========================================

        ladoIzquierdo.addLayout(
            generadorLayout
        )

        # ==========================================
        # PANEL DERECHO
        # ==========================================

        panel = QVBoxLayout()

        self.botonCursor = QPushButton("CURSOR")
        self.botonPause = QPushButton("PAUSE / STOP")
        self.botonReset = QPushButton("RESET")
        self.botonPower = QPushButton("POWER")

        botones = [
            self.botonCursor,
            self.botonPause,
            self.botonReset,
            self.botonPower
        ]

        for b in botones:

            b.setFixedHeight(60)

            b.setStyleSheet("""
                QPushButton{
                    background-color: #404040;
                    color: white;
                    font-size: 16px;
                    border-radius: 10px;
                }

                QPushButton:hover{
                    background-color: #606060;
                }
            """)

            panel.addWidget(b)

        # ==========================================
        # LABELS
        # ==========================================

        self.labelFreq = QLabel()
        self.labelAmp = QLabel()
        self.labelPeriodo = QLabel()
        self.labelCursor = QLabel("")

        labels = [
            self.labelFreq,
            self.labelAmp,
            self.labelPeriodo,
            self.labelCursor
        ]

        for l in labels:

            l.setStyleSheet("""
                color: cyan;
                background-color: black;
                font-size: 18px;
                padding: 8px;
            """)

            l.setMinimumHeight(70)

            panel.addWidget(l)

        # ==========================================
        # VOLTS/DIV
        # ==========================================

        textoVolt = QLabel(
            "VOLTS / DIV"
        )

        textoVolt.setStyleSheet("""
            color: black;
            background-color: lightgray;
            font-size: 18px;
            font-weight: bold;
            padding: 5px;
        """)

        panel.addWidget(textoVolt)

        self.dialVolt = QDial()

        self.dialVolt.setMinimum(1)
        self.dialVolt.setMaximum(400)
        self.dialVolt.setValue(20)

        panel.addWidget(
            self.dialVolt
        )

        # ==========================================
        # SEC/DIV
        # ==========================================

        textoTiempo = QLabel(
            "SEC / DIV"
        )

        textoTiempo.setStyleSheet("""
            color: black;
            background-color: lightgray;
            font-size: 18px;
            font-weight: bold;
            padding: 5px;
        """)

        panel.addWidget(textoTiempo)

        self.dialTiempo = QDial()

        self.dialTiempo.setMinimum(1)
        self.dialTiempo.setMaximum(300)
        self.dialTiempo.setValue(50)

        panel.addWidget(
            self.dialTiempo
        )

        # ==========================================
        # CONEXIONES
        # ==========================================

        self.botonPause.clicked.connect(
            self.togglePause
        )

        self.botonCursor.clicked.connect(
            self.toggleCursor
        )

        self.botonReset.clicked.connect(
            self.resetSignal
        )

        self.botonPower.clicked.connect(
            self.close
        )

        self.dialVolt.valueChanged.connect(
            self.cambiarEscalaVertical
        )

        self.dialTiempo.valueChanged.connect(
            self.cambiarEscalaHorizontal
        )

        # ==========================================
        # LAYOUTS
        # ==========================================

        mainLayout.addLayout(
            ladoIzquierdo,
            5
        )

        mainLayout.addLayout(
            panel,
            1
        )

        self.setLayout(
            mainLayout
        )

        # ==========================================
        # TIMER
        # ==========================================

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.updatePlot
        )

        self.timer.start(20)

    # ==========================================
    # UPDATE
    # ==========================================

    def updatePlot(self):

        t = np.linspace(
            self.xMin,
            self.xMax,
            3000
        )

        # ==========================================
        # GENERADOR OFF
        # ==========================================

        if not self.generadorON:

            y = np.zeros_like(t)

            self.curva.setData(t, y)

            self.labelFreq.setText(
                "Frecuencia: ---"
            )

            self.labelAmp.setText(
                "Amplitud: ---"
            )

            self.labelPeriodo.setText(
                "Periodo: ---"
            )

            return

        # ==========================================
        # ONDA
        # ==========================================

        y = self.amplitud * np.sin(
            2 * np.pi *
            self.frecuencia *
            (t + self.tiempo)
        )

        if not self.pausado:

            self.curva.setData(
                t,
                y
            )

            self.tiempo += 0.003

        # ==========================================
        # LABELS
        # ==========================================

        self.labelFreq.setText(
            f"Frecuencia: {self.frecuencia} Hz"
        )

        self.labelAmp.setText(
            f"Amplitud: {self.amplitud} V"
        )

        self.labelPeriodo.setText(
            f"Periodo: {1/self.frecuencia:.5f} s"
        )

    # ==========================================
    # CURSOR CLICK
    # ==========================================

    def mouseClicked(self, evt):

        if not self.cursorActivo:
            return

        pos = evt.scenePos()

        if self.plotWidget.sceneBoundingRect().contains(pos):

            mousePoint = self.plotWidget.plotItem.vb.mapSceneToView(pos)

            x = mousePoint.x()
            y = mousePoint.y()

            self.cursorV.setValue(x)
            self.cursorH.setValue(y)

            self.labelCursor.setText(
                f"Tiempo: {x:.6f} s\n"
                f"Voltaje: {y:.6f} V"
            )

    # ==========================================
    # GENERADOR
    # ==========================================

    def toggleGenerador(self):

        self.generadorON = not self.generadorON

        if self.generadorON:

            self.botonGenerador.setText(
                "GENERADOR: ON"
            )

            self.botonGenerador.setStyleSheet("""
                QPushButton{
                    background-color: green;
                    color: white;
                    font-size: 16px;
                    border-radius: 10px;
                    padding: 10px;
                }
            """)

        else:

            self.botonGenerador.setText(
                "GENERADOR: OFF"
            )

            self.botonGenerador.setStyleSheet("""
                QPushButton{
                    background-color: red;
                    color: white;
                    font-size: 16px;
                    border-radius: 10px;
                    padding: 10px;
                }
            """)

    # ==========================================
    # FRECUENCIA
    # ==========================================

    def actualizarFrecuencia(self):

        try:

            valor = float(
                self.inputFreq.text()
            )

            if valor > 0:

                self.frecuencia = valor

        except:
            pass

    # ==========================================
    # AMPLITUD
    # ==========================================

    def actualizarAmplitud(self):

        try:

            valor = float(
                self.inputAmp.text()
            )

            self.amplitud = valor

        except:
            pass

    # ==========================================
    # PAUSE
    # ==========================================

    def togglePause(self):

        if not self.generadorON:
            return

        self.pausado = not self.pausado

    # ==========================================
    # CURSOR
    # ==========================================

    def toggleCursor(self):

        if not self.generadorON:
            return

        self.cursorActivo = not self.cursorActivo

        if self.cursorActivo:

            self.cursorV.show()
            self.cursorH.show()

        else:

            self.cursorV.hide()
            self.cursorH.hide()

            self.labelCursor.setText("")

    # ==========================================
    # RESET
    # ==========================================

    def resetSignal(self):

        self.tiempo = 0

    # ==========================================
    # VOLTS/DIV
    # ==========================================

    def cambiarEscalaVertical(self, valor):

        escala = valor / 20

        if escala < 0.05:
            escala = 0.05

        self.plotWidget.setYRange(
            -escala,
            escala
        )

    # ==========================================
    # SEC/DIV
    # ==========================================

    def cambiarEscalaHorizontal(self, valor):

        escala = valor / 100

        if escala < 0.005:
            escala = 0.005

        self.xMax = escala

        self.plotWidget.setXRange(
            self.xMin,
            self.xMax
        )

        self.plotWidget.setLimits(
            xMin=self.xMin,
            xMax=self.xMax
        )


# ==============================================
# EJECUTAR
# ==============================================

app = QApplication(sys.argv)

window = Osciloscopio()

window.show()

sys.exit(app.exec())