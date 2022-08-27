/********************************
 * Custom Game Show
 * FormScoreEdit.Designer.cs
 * Created by Justin Leonard
********************************/

namespace CustomGameShow
{
    partial class FormScoreEdit
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(FormScoreEdit));
            this.buttonExit = new System.Windows.Forms.Button();
            this.labelTitle = new System.Windows.Forms.Label();
            this.labelScore0 = new System.Windows.Forms.Label();
            this.labelScore1 = new System.Windows.Forms.Label();
            this.labelScore2 = new System.Windows.Forms.Label();
            this.comboBoxContestant = new System.Windows.Forms.ComboBox();
            this.buttonSaveScore = new System.Windows.Forms.Button();
            this.numericUpDownScore = new System.Windows.Forms.NumericUpDown();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownScore)).BeginInit();
            this.SuspendLayout();
            // 
            // buttonExit
            // 
            this.buttonExit.BackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonExit.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("buttonExit.BackgroundImage")));
            this.buttonExit.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.buttonExit.Cursor = System.Windows.Forms.Cursors.Hand;
            this.buttonExit.FlatAppearance.BorderColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonExit.FlatAppearance.BorderSize = 0;
            this.buttonExit.FlatAppearance.MouseDownBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonExit.FlatAppearance.MouseOverBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonExit.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonExit.Font = new System.Drawing.Font("Arial", 36F, System.Drawing.FontStyle.Bold);
            this.buttonExit.Location = new System.Drawing.Point(91, 469);
            this.buttonExit.Name = "buttonExit";
            this.buttonExit.Size = new System.Drawing.Size(468, 75);
            this.buttonExit.TabIndex = 0;
            this.buttonExit.TabStop = false;
            this.buttonExit.Text = "Exit";
            this.buttonExit.UseVisualStyleBackColor = false;
            this.buttonExit.Click += new System.EventHandler(this.buttonExit_Click);
            // 
            // labelTitle
            // 
            this.labelTitle.AutoSize = true;
            this.labelTitle.Font = new System.Drawing.Font("Arial Black", 48F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelTitle.ForeColor = System.Drawing.SystemColors.ControlText;
            this.labelTitle.Location = new System.Drawing.Point(126, 6);
            this.labelTitle.Name = "labelTitle";
            this.labelTitle.Size = new System.Drawing.Size(401, 90);
            this.labelTitle.TabIndex = 0;
            this.labelTitle.Text = "Edit Score";
            // 
            // labelScore0
            // 
            this.labelScore0.AutoSize = true;
            this.labelScore0.Font = new System.Drawing.Font("Arial", 36F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelScore0.Location = new System.Drawing.Point(12, 100);
            this.labelScore0.Name = "labelScore0";
            this.labelScore0.Size = new System.Drawing.Size(187, 56);
            this.labelScore0.TabIndex = 0;
            this.labelScore0.Text = "Default";
            // 
            // labelScore1
            // 
            this.labelScore1.AutoSize = true;
            this.labelScore1.Font = new System.Drawing.Font("Arial", 36F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelScore1.Location = new System.Drawing.Point(12, 172);
            this.labelScore1.Name = "labelScore1";
            this.labelScore1.Size = new System.Drawing.Size(187, 56);
            this.labelScore1.TabIndex = 0;
            this.labelScore1.Text = "Default";
            // 
            // labelScore2
            // 
            this.labelScore2.AutoSize = true;
            this.labelScore2.Font = new System.Drawing.Font("Arial", 36F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelScore2.Location = new System.Drawing.Point(12, 244);
            this.labelScore2.Name = "labelScore2";
            this.labelScore2.Size = new System.Drawing.Size(187, 56);
            this.labelScore2.TabIndex = 0;
            this.labelScore2.Text = "Default";
            // 
            // comboBoxContestant
            // 
            this.comboBoxContestant.BackColor = System.Drawing.SystemColors.Control;
            this.comboBoxContestant.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.comboBoxContestant.Font = new System.Drawing.Font("Arial", 27.75F, System.Drawing.FontStyle.Bold);
            this.comboBoxContestant.FormattingEnabled = true;
            this.comboBoxContestant.Location = new System.Drawing.Point(91, 319);
            this.comboBoxContestant.Name = "comboBoxContestant";
            this.comboBoxContestant.Size = new System.Drawing.Size(268, 52);
            this.comboBoxContestant.TabIndex = 0;
            this.comboBoxContestant.TabStop = false;
            this.comboBoxContestant.SelectedIndexChanged += new System.EventHandler(this.comboBoxContestant_SelectedIndexChanged);
            // 
            // buttonSaveScore
            // 
            this.buttonSaveScore.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("buttonSaveScore.BackgroundImage")));
            this.buttonSaveScore.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.buttonSaveScore.Cursor = System.Windows.Forms.Cursors.Hand;
            this.buttonSaveScore.FlatAppearance.BorderColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonSaveScore.FlatAppearance.BorderSize = 0;
            this.buttonSaveScore.FlatAppearance.CheckedBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonSaveScore.FlatAppearance.MouseDownBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonSaveScore.FlatAppearance.MouseOverBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonSaveScore.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonSaveScore.Font = new System.Drawing.Font("Arial", 27.75F, System.Drawing.FontStyle.Bold);
            this.buttonSaveScore.Location = new System.Drawing.Point(91, 394);
            this.buttonSaveScore.Name = "buttonSaveScore";
            this.buttonSaveScore.Size = new System.Drawing.Size(468, 50);
            this.buttonSaveScore.TabIndex = 0;
            this.buttonSaveScore.TabStop = false;
            this.buttonSaveScore.Text = "Save";
            this.buttonSaveScore.UseVisualStyleBackColor = true;
            this.buttonSaveScore.Click += new System.EventHandler(this.buttonSaveScore_Click);
            // 
            // numericUpDownScore
            // 
            this.numericUpDownScore.Font = new System.Drawing.Font("Arial", 27.75F, System.Drawing.FontStyle.Bold);
            this.numericUpDownScore.Location = new System.Drawing.Point(388, 320);
            this.numericUpDownScore.Maximum = new decimal(new int[] {
            999,
            0,
            0,
            0});
            this.numericUpDownScore.Name = "numericUpDownScore";
            this.numericUpDownScore.ReadOnly = true;
            this.numericUpDownScore.Size = new System.Drawing.Size(171, 50);
            this.numericUpDownScore.TabIndex = 0;
            this.numericUpDownScore.TabStop = false;
            this.numericUpDownScore.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // FormScoreEdit
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ScrollBar;
            this.ClientSize = new System.Drawing.Size(650, 572);
            this.Controls.Add(this.numericUpDownScore);
            this.Controls.Add(this.buttonSaveScore);
            this.Controls.Add(this.comboBoxContestant);
            this.Controls.Add(this.labelScore2);
            this.Controls.Add(this.labelScore1);
            this.Controls.Add(this.labelScore0);
            this.Controls.Add(this.labelTitle);
            this.Controls.Add(this.buttonExit);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.KeyPreview = true;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "FormScoreEdit";
            this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Custom Game Show";
            this.Load += new System.EventHandler(this.FormScoreEdit_Load);
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.FormScoreEdit_KeyDown);
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownScore)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button buttonExit;
        private System.Windows.Forms.Label labelTitle;
        private System.Windows.Forms.Label labelScore0;
        private System.Windows.Forms.Label labelScore1;
        private System.Windows.Forms.Label labelScore2;
        private System.Windows.Forms.ComboBox comboBoxContestant;
        private System.Windows.Forms.Button buttonSaveScore;
        private System.Windows.Forms.NumericUpDown numericUpDownScore;
    }
}